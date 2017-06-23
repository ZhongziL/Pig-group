from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField

class PostForm(FlaskForm):
    post = StringField('post')
    picture = FileField('picture')
    submit = SubmitField('submit')