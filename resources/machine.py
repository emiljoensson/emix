from flask import abort
from flask_restful import Resource
from models import *

class MachineAPI(Resource):
    def get(self, id):
        machine = Machine.query.filter(Machine.id == id).first()
        machine_schema = MachineSchema()
        json = machine_schema.dump(machine).data
        if machine is None:
            abort(404, {'message': 'machine not found'})
        return json, 200
