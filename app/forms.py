from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import InputRequired

class AddBookForm(FlaskForm):
    ''' Form for adding a new book '''
    title = StringField('Title:', validators=[InputRequired()])
    author = StringField('Author:', validators=[InputRequired()])
    genre_id = SelectField('Genre:', validators=[InputRequired()])
    submit = SubmitField('Add book')

class EditBookForm(AddBookForm):
    ''' Form for editing an existing book '''
    submit = SubmitField('Save changes')

class AddGenreForm(FlaskForm):
    ''' Form for adding a new genre '''
    name = StringField('Name:', validators=[InputRequired()])
    submit = SubmitField('Add genre')

class EditGenreForm(AddGenreForm):
    ''' Form for editing an existing genre '''
    submit = SubmitField('Save changes')
