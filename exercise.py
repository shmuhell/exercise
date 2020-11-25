from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import render_template, abort
import pandas as pd
import ast
import json



app = Flask(__name__)
api = Api(app)


class Users(Resource): 
    def get(self):
        data = pd.read_json('users.json')  
        data = data.to_dict()
        for element in data.values():
            if 'id' in element:
                del element['id']
        return data, 200  
    pass


class User(Resource):
    def get(self,username):
        data = pd.read_json('users.json')
        data = data.to_dict()
        if username in data.keys():
            return data[username], 200 
        else:
             abort(404)
    pass

api.add_resource(Users, '/users') 
api.add_resource(User, '/user/<username>',endpoint='username')  




if __name__ == '__main__':
    app.run(host = '0.0.0.0')  