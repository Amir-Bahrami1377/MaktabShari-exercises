from app import db

class User(db.Model):
    id = db.column(db.Integer, primary_key=True)
