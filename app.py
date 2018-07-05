import os
from flask import Flask, abort
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database stuff
from database import db_session, init_db
from models import *

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# initalize/build the db
init_db()

# for debug only:
#one = Machine('test.com', 'debian-8-64')
#two = Machine('example.com', 'centos-7-64')
#db_session.add(one)
#db_session.add(two)
#db_session.commit()
print(Machine.query.all())


class Index(Resource):
    def get(self):
        return {'hello': 'world'}

class MachineAPI(Resource):
    def get(self, id):
        machine = Machine.query.filter(Machine.id == id).first()
        machine_schema = MachineSchema()
        json = machine_schema.dump(machine).data
        if machine is None:
            abort(404, {'message': 'machine not found'})
        return json, 200

api.add_resource(Index, '/')
api.add_resource(MachineAPI, '/machine/<int:id>')

if __name__ == '__main__':
    print("ENVIRONMENT: ", os.environ['APP_SETTINGS'])
    app.run()
