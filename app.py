# Libraries
import os
from flask import Flask, abort
from flask_restful import Api

# Custom modules
from resources import *


app = Flask(__name__)
api = Api(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Database stuff
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

api.add_resource(MachineAPI, '/machine/<int:id>')

if __name__ == '__main__':
    print("ENVIRONMENT: ", os.environ['APP_SETTINGS'])
    app.run()
