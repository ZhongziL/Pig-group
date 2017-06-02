from . import main
from flask import render_template, abort
from flask_login import login_required
from ..models import User, Permission


@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/<name>')
@login_required
def user(name):
    u = User.query.filter_by(username=name).first()
    if u is None:
        abort(404)
    return render_template('profile.html', user=u)
