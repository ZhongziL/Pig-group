from . import auth
from flask import url_for, render_template, redirect, flash, request, session
from .forms import LoginForm, RegisterForm_email, ChangePasswordForm, EditProfileForm
from .forms import ChangeEmailForm, ResetPasswordForm, ResetForm_tel, EditProfileAdminForm
from .forms import LoginForm_telnumber, RegisterForm_telnumber, ResetForm_email
from ..models import User
from sqlalchemy import or_
from .. import db
from flask_login import login_user, logout_user, login_required, current_user
from ..email import send_mail
from ..decorator import admin_required
from ..sms import send_out
import random


@auth.before_app_request
def before():
    if current_user.is_authenticated:
        current_user.ping()
        if request.endpoint == 'auth.login':
            flash('please logout first')
            return redirect(url_for('main.index'))
        if not current_user.confirmed \
                and request.endpoint != 'main.index' \
                and request.endpoint != 'auth.unconfirmed' \
                and request.endpoint != 'auth.logout' \
                and request.endpoint != 'auth.confirm' \
                and request.endpoint != 'auth.resend_confirm':
            return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username_email = form.username_email.data
        password = form.password.data
        user = User.query.filter(or_(User.username == username_email,
                                    User.email == username_email,
                                     User.telnumber == username_email)).first()

        if user is not None and user.checkpassword(password):
            login_user(user)
            flash('login success')
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('username or password error')
            return render_template('/auth/login.html', form=form)
    else:
        return render_template('/auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm_email()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        user = User.query.filter(or_(User.username == username, User.email == email)).first()

        if user is None:
            u = User(username=username, email=email, password=password)
            token = u.generation_confirmation_token()
            send_mail(email, username, 'email_to_client', token=token, username=u.username)
            db.session.add(u)
            flash('register success')
            return redirect(url_for('auth.login'))
        else:
            flash('username or email is already existed')
            return render_template('/auth/register.html', form=form)
    else:
        return render_template('/auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    flash('logout success')
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        old_password = form.oldpassword.data
        if current_user.checkpassword(old_password):
            current_user.password = form.newpassword.data
            db.session.add(current_user)
            flash('password changed')
            return redirect(url_for('main.index'))
        flash('password error')
        return render_template('/auth/changepassword.html', form=form)
    return render_template('/auth/changepassword.html', form=form)


@auth.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        user_detail = form.user_detail.data
        current_user.user_detail = user_detail
        db.session.add(current_user)
        flash('profile edit success')
        return redirect(url_for('main.user', name=current_user.username))
    form.user_detail.data = current_user.user_detail
    return render_template('/auth/edit_profile.html', form=form, user=current_user)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('confirmed success')
    else:
        flash('error')
    return redirect(url_for('main.index'))


@auth.route('/confirm')
@login_required
def resend_confirm():
    token = current_user.generation_confirmation_token()
    send_mail(current_user.email, current_user.username,
              'email_to_client', token=token, username=current_user.username)
    flash('resend')
    return redirect(url_for('auth.unconfirmed'))


@auth.route('/change-email', methods=['GET', 'POST'])
@login_required
def change_email():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        if current_user.checkpassword(form.password.data):
            current_user.email = form.new_email.data
            current_user.confirmed = False
            token = current_user.generation_confirmation_token()
            send_mail(current_user.email, current_user.username,
                      'email_to_client', token=token, username=current_user.username)
            db.session.add(current_user)
            flash('your email has already been changed')
            return redirect(url_for('auth.unconfirmed'))
        flash('password error')
        return render_template('/auth/change_email.html', form=form)
    return render_template('/auth/change_email.html', form=form)


@auth.route('/reset_by_email', methods=['GET', 'POST'])
def reset_password_email():
    form = ResetForm_email()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            token = user.generation_reset_token()
            send_mail(form.email.data, user.username,
                      'email_to_reset', token=token, username=user.username)
            flash('send email')
            return redirect(url_for('auth.login'))
        flash('email is not exist')
        return render_template('/auth/reset_password.html', form=form)
    return render_template('/auth/reset_password.html', form=form)


@auth.route('/reset_by_tel', methods=['GET', 'POST'])
def reset_password_tel():
    form = ResetForm_tel()
    if request.method == 'POST':
        user = User.query.filter_by(telnumber=form.telnumber.data).first()
        if user is None:
            flash('telnumber is not exist')
            return render_template('/auth/reset_by_tel.html', form=form)
        if 'send' in request.form:
            code = random.randint(1000,9999)
            text = str(code)
            session['code'] = text
            print(text)
            mobile = form.telnumber.data
            send_out(text, mobile)
            return render_template('/auth/reset_by_tel.html', form=form)
        elif 'submit' in request.form:
            if form.validatecode.data == session['code']:
                return redirect(url_for('auth.reset_by_num', mobile=form.telnumber.data))
            return render_template('/auth/reset_by_tel.html', form=form)
        return render_template('/auth/reset_by_tel.html', form=form)
    return render_template('/auth/reset_by_tel.html', form=form)


@auth.route('/reset_num/<mobile>', methods=['GET','POST'])
def reset_by_num(mobile):
    form = ResetPasswordForm()
    user = User.query.filter_by(telnumber=mobile).first()
    if form.validate_on_submit() and user is not None and mobile is not None:
        user.password = form.newpassword.data
        db.session.add(user)
        flash('reset success')
        return redirect(url_for('auth.login'))
    if user is None or mobile is None:
        flash('error, please try again')
        return redirect(url_for('auth.reset_password_tel'))
    return render_template('/auth/password_reset.html', form=form, email=mobile)


@auth.route('/reset/<token>', methods=['GET', 'POST'])
def reset_confirm(token):
    email = User.reset_password(token)
    form = ResetPasswordForm()
    user = User.query.filter_by(email=email).first()
    if form.validate_on_submit() and user is not None and email is not None:
        user.password = form.newpassword.data
        db.session.add(user)
        flash('reset success')
        return redirect(url_for('auth.login'))
    if user is None or email is None:
        flash('error, please try again')
        return redirect(url_for('auth.reset_password_email'))
    return render_template('/auth/password_reset.html', form=form, email=email)


@auth.route('/edit_profile_admin/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.confirmed = form.confirmed.data
        user.telnumber = form.telnumber.data
        user.user_detail = form.user_detail.data
        db.session.add(user)
        flash('edit success')
        return redirect(url_for('main.user', user=user))
    form.username.data = user.username
    form.email.data = user.email
    form.confirmed.data = user.confirmed
    form.telnumber.data = user.telnumber
    form.user_detail.data = user.user_detail
    return render_template('/auth/edit_profile_admin.html', form=form, user=user)


@auth.route('/register_by_telnumber', methods=['GET','POST'])
def register_by_tel():
    form = RegisterForm_telnumber()
    if request.method == 'POST':
        if 'send' in request.form:
            code = random.randint(1000,9999)
            text = str(code)
            session['code'] = text
            print(text)
            mobile = form.telnumber.data
            send_out(text, mobile)
            return render_template('/auth/register_by_tel.html', form=form)
        elif 'submit' in request.form:
            if form.validatecode.data == session['code']:
                user = User(username=form.username.data, telnumber=form.telnumber.data,
                            password=form.password.data, confirmed=True)
                db.session.add(user)
                return redirect(url_for('auth.login'))
            return render_template('/auth/register_by_tel.html', form=form)
        return render_template('/auth/register_by_tel.html', form=form)
    return render_template('/auth/register_by_tel.html', form=form)