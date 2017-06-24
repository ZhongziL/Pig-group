from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField

class PostForm(FlaskForm):
    title = StringField('title')
    picture = FileField('picture')
    context = TextAreaField('body')
    submit = SubmitField('submit')

class CommentForm(FlaskForm):
    ansText = TextAreaField('body')
    submit = SubmitField('submit')