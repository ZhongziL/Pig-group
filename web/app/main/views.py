from . import main
from flask import render_template, abort, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import User, Permission, Post
from .forms import PostForm
from .. import db


@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)


@main.route('/')
def index():
    form = PostForm()
    if current_user.is_authenticated:
        if current_user.can(Permission.WRITE_ARITICLES) and request.method == 'POST':
            post = Post(body=form.post.data, author_name=current_user._get_current_object())
            db.session.add(post)
            return redirect(url_for('main.index'))
    '''posts = Post.query.order_by(Post.timestamp.desc()).all()'''

    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=20, error_out=False)
    posts = pagination.items
    return render_template('index.html', form=form, posts=posts, pagination=pagination)


@main.route('/user/<name>')
@login_required
def user(name):
    u = User.query.filter_by(username=name).first()
    if u is None:
        abort(404)
    '''posts = u.posts.order_by(Post.timestamp.desc()).all()'''
    page = request.args.get('page', 1, type=int)
    pagination = u.posts.order_by(Post.timestamp.desc()).paginate(page, per_page=20, error_out=False)
    posts = pagination.items
    return render_template('profile.html', user=u, posts=posts, pagination=pagination)
