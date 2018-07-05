#! /usr/bin/env python3
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow
from database import Base

ma = Marshmallow()

""""
Class: Machine
"""
class Machine(Base):
    __tablename__ = 'machine'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50), unique=False)
    image = Column(String(50), unique=False)

    def __init__(self, hostname=None, image=None):
        self.hostname = hostname
        self.image = image

    def __repr__(self):
        return "<Machine(id='%s', hostname='%s', image='%s')>" % (self.id, self.hostname, self.image)

# Marshmallow class used to serialize query output to JSON
class MachineSchema(ma.ModelSchema):
    class Meta:
        # Fields to expose
        fields = ('id', 'hostname', 'image')