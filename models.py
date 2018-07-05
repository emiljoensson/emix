from sqlalchemy import Column, Integer, String
from database import Base, ma

class Machines(Base):
    __tablename__ = 'machines'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50), unique=False)
    image = Column(String(50), unique=False)

    def __init__(self, hostname=None, image=None):
        self.hostname = hostname
        self.image = image

    def __repr__(self):
        return "<Machine(id='%s', hostname='%s', image='%s')>" % (self.id, self.hostname, self.image)

class MachinesSchema(ma.ModelSchema):
    class Meta:
        model = Machines
