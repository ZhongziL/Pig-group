from . import main
from flask import render_template, abort, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import User, Permission, Post, Comment
from .forms import PostForm, CommentForm
from .. import db


@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)


@main.route('/')
def index():
    if current_user.is_authenticated :
        picSrc = current_user.avatar_url
        username=current_user.username
    else:
        picSrc = "avatar/head.png"
        username=" "
    # page = request.args.get('page', 1, type=int)
    # pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=20, error_out=False)
    # posts = pagination.items
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    number = Post.query.count()
    if number > 5:
        onshows = posts[:4]
    else:
        onshows = posts
    return render_template('main/index.html', posts=posts,
                           onshows=onshows, username=username, picSrc=picSrc)


@main.route('/user/<name>')
@login_required
def user(name):
    u = User.query.filter_by(username=name).first()
    if u is None:
        abort(404)
    posts = u.posts.order_by(Post.timestamp.desc()).all()
    answers = u.comments.order_by(Comment.timestamp.desc()).all()
    list = []
    for answer in answers:
        p = Post.query.filter_by(id=answer.post_id).first()
        list.append(p)
    # page = request.args.get('page', 1, type=int)
    # pagination = u.posts.order_by(Post.timestamp.desc()).paginate(page, per_page=20, error_out=False)
    # posts = pagination.items
    followeds = u.followed.all()
    followers = u.followers.all()
    return render_template('main/personal.html', user=u, articles=posts, answers=list,cuser=current_user,
                           followeds=followeds, followers=followers)


@main.route('/writeEssay', methods=['GET','POST'])
@login_required
def writeEssay():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.context.data
        if title != "" and content != "":
            post = Post(body=title, body_html=content, good_count=0, author_name=current_user.username)
            db.session.add(post)
            return redirect(url_for('main.index'))
        return redirect(url_for('main.writeEssay'))
    return render_template('main/writeEssay.html', form=form, username=current_user.username, picSrc=current_user.avatar_url)


@main.route('/recommend')
@login_required
def recommend():
    post = Post.query.all()
    number = Post.query.count()
    if number >= 10:
        recommends = post[:9]
    else :
        recommends = post
    return render_template('main/recommend.html', picSrc=current_user.avatar_url,
                           username=current_user.username, recommends=recommends)


@main.route('/questionDetail/<int:id>', methods=['GET','POST'])
@login_required
def question(id):
    form = CommentForm()
    post = Post.query.get_or_404(id)
    if form.validate_on_submit():
        comment = form.ansText.data
        if comment != "":
            c = Comment(body=comment, author_name=current_user.username, post_id=post.id, good_count=0)
            db.session.add(c)
            return redirect(url_for('main.question', id=post.id))

    comments = post.comments.all()
    number = Post.query.count()
    posts = Post.query.all()
    if number >= 5:
        onshows = posts[:4]
    else:
        onshows = posts
    return render_template('main/questionDetail.html', picSrc=current_user.avatar_url,
                           form=form, post=post, username=current_user.username, comments=comments, onshows=onshows)


@main.route('/addPost/<int:id>')
@login_required
def addPost(id):
    post = Post.query.get_or_404(id)
    post.good_count = post.good_count+1
    db.session.add(post)
    return redirect(url_for('main.index'))


@main.route('/addComment/<int:id>')
@login_required
def addComment(id):
    comment = Comment.query.get_or_404(id)
    comment.good_count = comment.good_count+1
    db.session.add(comment)
    return redirect(url_for('main.question', id=comment.post_id))


@main.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is not None:
        current_user.follow(user)
        db.session.add(current_user)
    return redirect(url_for('main.user', name=username))


@main.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is not None:
        current_user.unfollow(user)
        db.session.add(current_user)
    return redirect(url_for('main.user', name=username))
