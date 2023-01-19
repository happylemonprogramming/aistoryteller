from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Necessary class to have a form on HTML for POST
class CommentForm(FlaskForm):
  comment =  StringField('''Once upon a time...''', validators=[DataRequired()])
  submit = SubmitField("Create")