from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FileField, RadioField
from wtforms.validators import Email, EqualTo, Length, Regexp, DataRequired
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    username_email = StringField('username_email')
    password = StringField('password')
    submit = SubmitField('Log In')

class LoginForm_telnumber(FlaskForm):
    telnumber = StringField('telnumber')
    password = StringField('password')
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
    inputOriginalPassword = StringField('oldpassword')
    inputPassword = StringField('newpassword')
    inputConfirmPassword = StringField('password_again')
    submit = SubmitField('Change Confirm')


class EditProfileForm(FlaskForm):
    inputNick = StringField('username')
    upload = FileField('avatar')
    user_detail = StringField('userdetail')
    submit = SubmitField('Confirm')


class ChangeEmailForm(FlaskForm):
    inputEmail = StringField('email')
    submit = SubmitField('Change Email')


class ChangeTelForm(FlaskForm):
    inputPhone = StringField('telnumber')
    send = SubmitField('send')
    inputVcode = StringField('code')
    submit = SubmitField('submit')


class ResetForm_email(FlaskForm):
    email = StringField('email')
    submit = SubmitField('Reset Password')


class ResetForm_tel(FlaskForm):
    telnumber = StringField('telnumber')
    send = SubmitField('Send Message')
    validatecode = StringField('code')
    submit = SubmitField('Reset Password')


class ResetPasswordForm(FlaskForm):
    password = StringField('password')
    password_again = StringField('password_again')
    submit = SubmitField('Change Confirm')


class EditProfileAdminForm(FlaskForm):
    username = StringField('username')
    email = StringField('email')
    telnumber = StringField('telnumber')
    confirmed = BooleanField('confirmed')
    user_detail = StringField('userdetail')
    submit = SubmitField('Submit')


class UploadAvatarForm(FlaskForm):
    avatar = FileField('avatar')
    submit = SubmitField('Upload')