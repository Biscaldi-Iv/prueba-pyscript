from flask import Flask, render_template
from controllers.routes import global_scope
from flask_sqlalchemy import SQLAlchemy
from database import db_session, init_db
from controllers.api import api_bp

app = Flask(__name__)
app.secret_key = 'www123456www'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


app.register_blueprint(global_scope, url_prefix='')
app.register_blueprint(api_bp)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
