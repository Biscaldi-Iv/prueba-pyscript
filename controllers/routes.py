from crypt import methods
from flask import Blueprint, request, redirect, url_for, session, render_template
from sqlalchemy import null
from models.Models import User, Client
from database import engine
from sqlalchemy.orm import sessionmaker
import datetime

global_scope = Blueprint('PyTools', __name__, template_folder='templates')
DBSession = sessionmaker(engine, autocommit=False)


def _(s: str):
    """Hardcode til we add Babel"""
    return s


@global_scope.before_request
def SessionCheck():
    _, endp = request.endpoint.split('.')
    if endp != 'SignIn' and endp != 'Register' and endp != 'logout':
        try:
            lastinteraction = session['lastinteraction'].replace(tzinfo=None)
            sincelast = (datetime.datetime.now() - lastinteraction).seconds/60
            # http session lasts 10 minutes
            if session['user'] is None or sincelast > 10:
                return redirect(url_for('PyTools.logout'))
        except:
            return redirect('/logout')
        # http session time restart every request
        lastinteraction = datetime.datetime.now()
        session['lastinteraction'] = lastinteraction


@global_scope.route('/home', methods=['get', 'post'])
def Home():
    user = session['user']
    context = {'_': _, 'user': user}
    return render_template('home/index.html', **context)


@global_scope.route('/SignIn', methods=['get', 'post'])
def SignIn():
    context = {'_': _}
    if request.method == 'POST':
        usr = request.form['floatingInput']
        pwrd = request.form['floatingPassword']
        DB = DBSession()
        u = DB.query(User).filter_by(username=usr, password=pwrd).first()
        if type(u) is User:
            session['user'] = u.username
            session['lastinteraction'] = datetime.datetime.now()
            context.update({'user': u})
            return redirect(url_for('PyTools.Home'))
        else:
            error = 'Incorrect password or username'
    return render_template('SignIn/index.html', **context)


@global_scope.route('/Register', methods=['get', 'post'])
def Register():
    context = {'_': _}
    lastdata = User(username='', fullname='', password='')
    if request.method == 'POST':
        usr = request.form['username']
        fname = request.form['name']
        pwrd = request.form['password']
        lastdata = User(username=usr, fullname=fname, password=pwrd)
        DB = DBSession()
        u = DB.query(User).filter_by(username=usr).first()
        if type(u) is User and u.username == usr:
            error = f'Username {usr} is not allowed, try another name'
            context.update({'error': error})
        else:
            DB.add(lastdata)
            DB.commit()
            session['user'] = lastdata.username
            session['lastinteraction'] = datetime.datetime.now()
            return redirect(url_for('PyTools.Home'))
    context.update({'lastdata': lastdata})
    return render_template('register/index.html', **context)


@global_scope.route('/Stadistics', methods=['get', 'post'])
def Stadistics():
    context = {'_': _}
    return render_template('stadistics/index.html', **context)


@global_scope.route('/logout', methods=['get', 'post'])
def logout():
    session['user'] = None
    return redirect(url_for('PyTools.SignIn'))


@global_scope.route('/clients', methods=['get'])
def clients():
    context = {'_': _, 'user': session['user']}
    return render_template('clients/index.html', **context)
