from tokenize import Hexnumber
from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class SubcontractorsModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    subcontractor_id = db.Column(db.Integer(),unique = True)
    company = db.Column(db.String())
    type = db.Column(db.String())
    human_resources = db.Column(db.Integer())
    technical_rating = db.Column(db.Integer())
 
    def __init__(self, subcontractor_id,company,type,human_resources,technical_rating):
        self.subcontractor_id = subcontractor_id
        self.company = company
        self.type = type
        self.human_resources = human_resources
        self.technical_rating = technical_rating
 
    def __repr__(self):
        return f"{self.company}:{self.subcontractor_id}"