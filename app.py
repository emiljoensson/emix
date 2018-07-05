import os
from flask import Flask, abort
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database stuff
from database import db_session, init_db
from models import Machines, MachinesSchema

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# initalize/build the db
init_db()
#print(Machines.query.all())

class Index(Resource):
    def get(self):
        return {'hello': 'world'}

class Machine(Resource):
    def get(self, id):
        machine = Machines.query.filter(Machines.id == id).first()
        machine_schema = MachinesSchema()
        json = machine_schema.dump(machine).data
        if machine is None:
            abort(404, {'message': 'machine '})
        return json, 200

api.add_resource(Index, '/')
api.add_resource(Machine, '/machine/<int:id>')

if __name__ == '__main__':
    print("ENVIRONMENT: ", os.environ['APP_SETTINGS'])
    app.run()
