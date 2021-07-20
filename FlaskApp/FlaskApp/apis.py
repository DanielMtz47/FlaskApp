from flask_restful import Resource, Api
from FlaskApp import app
import pandas as pd

api = Api(app)

class SubnetAPI(Resource):
    def get(self):
        prefix = "192.1.3.01"
        subnet = "255.255.1.0"
        return {'subnet': subnet,
                'ip': prefix}

api.add_resource(SubnetAPI, '/getSubnet')