from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FileField, RadioField
from wtforms.validators import Email, EqualTo, Length, Regexp, DataRequired
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    username_email = StringField('username_email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class LoginForm_telnumber(FlaskForm):
    telnumber = StringField('telnumber', validators=[DataRequired(), Length(11), Regexp('^[1-9][0-9]*&')])
    password = StringField('password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    username = StringField('username')
    email = StringField('email')
    telnumber = StringField('telnumber')
    send = SubmitField('Send Message')
    code = StringField('code')
    password = StringField('password')
    password_confirm = StringField('confirm_password')
    submit = SubmitField('Register')

class RegisterForm_telnumber(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    telnumber = StringField('telnumber', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    password_confirm = StringField('confirm_password')
    send = SubmitField('Send Message')
    validatecode = StringField('code', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username is already exist')

    def validate_telnumber(self, field):
        if User.query.filter_by(telnumber=field.data).first():
            raise ValidationError('telnumber has already been registered')

class ChangePasswordForm(FlaskForm):
    oldpassword = StringField('oldpassword', validators=[DataRequired()])
    newpassword = StringField('newpassword', validators=[DataRequired()])
    password_again = StringField('password_again', validators=[DataRequired()])
    submit = SubmitField('Change Confirm')


class EditProfileForm(FlaskForm):
    user_detail = StringField('userdetail')
    submit = SubmitField('Confirm')


class ChangeEmailForm(FlaskForm):
    new_email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    submit = SubmitField('Change Email')


class ResetForm_email(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    submit = SubmitField('Reset Password')


class ResetForm_tel(FlaskForm):
    telnumber = StringField('telnumber', validators=[DataRequired()])
    send = SubmitField('Send Message')
    validatecode = StringField('code', validators=[DataRequired()])
    submit = SubmitField('Reset Password')


class ResetPasswordForm(FlaskForm):
    newpassword = StringField('newpassword', validators=[DataRequired()])
    password_again = StringField('password_again', validators=[DataRequired()])
    submit = SubmitField('Change Confirm')


class EditProfileAdminForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    telnumber = StringField('telnumber', validators=[DataRequired(), Length(11), Regexp('^[1-9][0-9]*&')])
    confirmed = BooleanField('confirmed')
    user_detail = StringField('userdetail')
    submit = SubmitField('Submit')


class UploadAvatarForm(FlaskForm):
    avatar = FileField('avatar')
    submit = SubmitField('Upload')