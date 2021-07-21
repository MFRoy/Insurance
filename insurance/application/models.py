from . import db

class Car(db.Model):#car
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("owner.id"))

class Owner(db.Model):#owner
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    cars = db.relationship('Car', backref="owner")

# class Cover(db.Model):#cover
#     id = db.Column(db.Integer, primary_key=True)
#     details = db.Column(db.String(100), nullable=False)
#     cover_id = db.Column(db.Integer, db.ForeignKey("cover.id"), nullable=False, unique=True)