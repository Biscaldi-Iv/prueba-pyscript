from flask_restful import Resource, Api, marshal_with, fields, reqparse
from flask import Blueprint, request
from models.Models import Client, User
from controllers.routes import DBSession

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)


client_fields = {
    'id': fields.Integer,
    'bs_name': fields.String,
}

cli_parser = reqparse.RequestParser()
cli_parser.add_argument('id', type=int, help='client id')
cli_parser.add_argument('bs_name', type=str, help='client bs name')


class Clients(Resource):
    @marshal_with(client_fields)
    def post(self):
        js_data = request.json
        bsn_c = js_data['bs_name']
        DB = DBSession()
        cli = Client(bs_name=bsn_c)
        DB.add(cli)
        DB.commit()
        return cli.rep()

    @marshal_with(client_fields)
    def get(self, id):
        DB = DBSession()
        if id == 0:
            clis = DB.query(Client).all()
            return [x.rep() for x in clis]
        cli = DB.query(Client).filter_by(id=id).first()
        if cli is None:
            return 404
        rep = cli.rep()
        return rep

    @marshal_with(client_fields)
    def put(self):
        js_data = request.json
        ide = js_data['id']  # id of object to edit
        bsname = js_data['bs_name']  # new business name
        DB = DBSession()
        cli = DB.query(Client).filter_by(id=ide).first()
        if cli is None:
            return 404
        cli.bs_name = bsname
        DB.commit()
        rep = cli.rep()
        return rep

    @marshal_with(client_fields)
    def delete(self):
        js_data = request.json
        ide = js_data['id']  # id of object to delete
        DB = DBSession()
        cli = DB.query(Client).filter_by(id=ide).first()
        if cli is None:
            return 404
        rep = cli.rep().copy()
        DB.delete(cli)
        DB.commit()
        return rep


api.add_resource(Clients, '/Clients/<int:id>', '/Clients')
