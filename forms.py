from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

# Necessary class to have a form on HTML for POST
class CommentForm(FlaskForm):
  comment =  StringField('''Write a short Children's Story about...''', validators=[DataRequired()])
  # radio = RadioField('Post to Instagram?', choices=[('yes','Yes'), ('no','No')])
  submit = SubmitField("Create")