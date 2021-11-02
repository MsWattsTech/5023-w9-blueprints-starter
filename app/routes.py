from flask import render_template, redirect, url_for

from app import app, db
from app.models import Book, Genre
from app.forms import AddGenreForm, EditGenreForm

@app.route('/')
def index():
    return render_template('index.html', title = 'Home')



@app.route('/genres')
def genre_list():
    ''' A route for a list of all the genres in the collection. '''
    genres = Genre.query.all()
    return render_template('genre_list.html', title = 'Genres', genres = genres)

@app.route('/genres/add', methods = ['GET', 'POST'])
def genre_add():
    ''' A route for showing a form and processing form for adding a new genre. '''
    form = AddGenreForm()

    # When the form has been processed with no errors, save the new genre to database
    if form.validate_on_submit():
        genre = Genre()
        form.populate_obj(obj=genre)
        db.session.add(genre)
        db.session.commit()
        # Once the new genre has been saved, return back to the view of all genres
        return redirect(url_for('genre_list'))
    return render_template('genre_add.html', form = form, title = 'Add genre')

@app.route('/genres/<int:id>')
def genre_details(id):
    ''' A route to display details for a specific genre, for the given id. '''
    genre = Genre.query.get_or_404(id)
    return render_template('genre_details.html', title = 'Genre details', genre = genre)

@app.route('/genres/<int:id>/delete')
def genre_delete(id):
    ''' A route that deletes a genre for the given id. '''

    genre = Genre.query.get_or_404(id)
    db.session.delete(genre)
    db.session.commit()

    # Once the genre record has been deleted, return back to the list of the genres
    return redirect(url_for('genre_list'))

@app.route('/genres/<int:id>/edit', methods = ['GET', 'POST'])
def genre_edit(id):
    ''' A route for displaying and processing a form, when editing a genre. '''
   
    genre = Genre.query.get_or_404(id)
    form = EditGenreForm(obj=genre)

    # When the form has been completed correctly, the changes to the genre are saved
    if form.validate_on_submit():
        form.populate_obj(obj=genre)
        db.session.commit()
        # Once the changes have been saved in database, show the view of the details for the genre
        return redirect(url_for('genre_details', id = genre.id))
    
    # When the request is a GET or there are errors in the form, return the view with the form
    return render_template('genre_edit.html', title = 'Edit genre', form = form, genre = genre)

