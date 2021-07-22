import os, json
from flask_restful import Resource, Api
from FlaskApp import app

api = Api(app)

class SubnetAPI(Resource):
    def loadsubnetJSON(self):
        root_path = os.getcwd()
        data_path = os.path.join(root_path, "FlaskApp\static\data")
        with open(os.path.join(data_path, "virtualNetworks.json"), 'r') as f:
            self.jsdoc = json.load(f)

    def searchSubnet(self, ip):
        self.loadsubnetJSON()
        prefix = ip[:9]
        subnets = self.jsdoc["subnets"]
        for net in subnets:
            if(subnets[net]["addressPrefix"] == prefix):
                return net
        return "No subnet found"

    def get(self, ip):
        subnet = self.searchSubnet(ip)
        return {"ip": ip,
        "subnet": subnet}

api.add_resource(SubnetAPI, '/getSubnet/<ip>')



    

