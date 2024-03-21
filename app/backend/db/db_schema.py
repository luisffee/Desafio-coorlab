from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
import os
import json

db = SQLAlchemy()
engine = db.create_engine('postgresql://coorlab:coorlab@localhost/transports')

data = json.load(open('data.json'))

class InitDB():
    def __init__(self, app):
        self.app = app
        self.db = db
        self.engine = engine
        
    def createTables(self):
        self.db.create_all()
        
    def inject(self):
        for _, items in data.items():
            for item in items:
                data_loaded = Transports(**item)
                self.db.session.add(data_loaded)
                self.db.session.commit()

    def start(self):
        self.db.init_app(self.app)
        if not database_exists(self.engine.url): create_database(self.engine.url)
        if not os.path.exists('backend/db/injected.txt'):
            self.createTables()
            self.inject()
            # Create a file to mark that data has been injected
            with open('backend/db/injected.txt', 'w') as file:
                file.write('Data injected')
        return self.db

class Transports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price_confort = db.Column(db.String, nullable=False)
    price_econ = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    duration = db.Column(db.String, nullable=False)
    seat =db.Column(db.String, nullable=False)
    bed = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f'Transport: {self.name}'
        
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
