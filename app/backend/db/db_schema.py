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
                name = Companies.query.filter_by(name=item['name']).first()
                if not name:
                    name = Companies(name=item['name'])
                    self.db.session.add(name)
                    self.db.session.commit()
                city = Cities.query.filter_by(city=item['city']).first()
                if not city:
                    city = Cities(city=item['city'])
                    self.db.session.add(city)
                    self.db.session.commit()
                price_confort = float(item['price_confort'].split(' ')[1])
                price_econ = float(item['price_econ'].split(' ')[1])
                duration = int(item['duration'].split('h')[0])
                data_loaded = Travels(name=name, city=city, price_confort=price_confort, 
                                         price_econ=price_econ, duration=duration, 
                                         seat=item['seat'], bed=item['bed'])
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

class Travels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    price_confort = db.Column(db.Float, nullable=False)
    price_econ = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    seat = db.Column(db.String, nullable=False)
    bed = db.Column(db.String, nullable=False)

    name = db.relationship('Companies', backref='transports')
    city = db.relationship('Cities', backref='transports')

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, unique=True, nullable=False)
    
    def __init__(self, city):
        self.city = city
    
    def __repr__(self):
        return self.city

class Companies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name