from flask import render_template, redirect, url_for

from app import app, db
from app.book import bp
from app.models import Book
from .forms import AddBookForm, EditBookForm


@bp.route('/add', methods = ['GET', 'POST'])
def book_add():
    ''' A route for showing a form and processing form for adding a new book. '''
    
    form = AddBookForm()
    # Retrieve the different genres from the database, for display in a dropdown
    form.genre_id.choices = [(genre.id, genre.name) for genre in Genre.query.all()]

    # When the form has been submitted, process the form and save new book to database
    if form.validate_on_submit():
        book = Book()
        form.populate_obj(obj=book)
        db.session.add(book)
        db.session.commit()
        # Return back to the view that shows the list of books in the collection
        return redirect(url_for('book_list'))

    # When doing a GET request or there are errors in the form, return the view with the form
    return render_template('book.book_add.html', form = form, title = 'Add book')

@bp.route('/<int:id>/edit', methods = ['GET', 'POST'])
def book_edit(id):
    ''' A route for showing a form and processing form when editing a book. '''
    
    book = Book.query.get_or_404(id)
    form = EditBookForm(obj=book)
    # Retrieves all the genres from the database, to populate the genre dropdown
    form.genre_id.choices = [(genre.id, genre.name) for genre in Genre.query.all()]

    # When the form has been submitted, process the form and save changes to database
    if form.validate_on_submit():
        form.populate_obj(obj=book)
        db.session.commit()
        return redirect(url_for('book.book_details', id=book.id))

    # When doing a GET request or there are errors in the form, return the view with the form
    return render_template('book.book_edit.html', title = 'Book edit', form = form, book = book)

@bp.route('/')
def book_list():
    ''' A route for a list of all books in the collection. '''
    books = Book.query.all()
    return render_template('book.book_list.html', title = 'Books', books = books)

@bp.route('/<int:id>')
def book_details(id):
    ''' A route that shows the details for a specific book in the collection. '''
    book = Book.query.get_or_404(id)
    return render_template('book.book_details.html', title = 'Book details', book = book)


@bp.route('/<int:id>/delete')
def book_delete(id):
    ''' A route that retrieves and deletes a book for the given id. '''

    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()

    # Once the book is deleted, return back to the list of remaining books in collection
    return redirect(url_for('book.book_list'))