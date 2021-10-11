from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    books = db.relationship('Book', backref='genre')
