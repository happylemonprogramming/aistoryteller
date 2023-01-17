from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

# Necessary class to have a form on HTML for POST
class CommentForm(FlaskForm):
  comment =  StringField('''Write a short Children's Story about...''', validators=[DataRequired()])
  submit = SubmitField("Create")

class WhatNext(FlaskForm):
  radio = RadioField('You decide: ', choices=[('scary','Make it Scary'), ('heroic','Make it Heroic'), ('silly', 'Make it Silly')],validators=[DataRequired()])
  enter = SubmitField("Enter")