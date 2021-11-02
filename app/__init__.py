from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up configuration settings for connection to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

# The secret key here is used for demonstration purposes - DO NOT USE IN PRODUCTION
app.config['SECRET_KEY'] = 'this-is-a-secret' 

from app import routes
from app.models import Book, Genre

# TODO: Register blueprints for books and genre blueprints here
from app.book import bp as book_bp
app.register_blueprint(book_bp, url_prefix='/book')

@app.cli.command('init-db')
def init_db():

    # Recreate the database for the app
    db.drop_all()
    db.create_all()

    # Create some records for the different genres
    fantasy = Genre(
        name = 'Fantasy'
    )
    db.session.add(fantasy)

    programming = Genre(
        name = 'Programming'
    )
    db.session.add(programming)

    research = Genre(
        name = 'Research'
    )
    db.session.add(research)

    # Create some records for the different books
    hobbit = Book(
        title = 'The Hobbit',
        author = 'J.R.R Tolkien',
        genre = fantasy
    )

    python = Book(
        title = 'Automate the Boring Stuff with Python',
        author = 'Al Sweigart',
        genre = programming
    )

    research_skills = Book(
        title = 'Research Skills for Teachers',
        author = 'Beverley Moriarty',
        genre = research
    )

    db.session.commit()
