from datetime import datetime  #关于渲染时间的一个变量
from flask import render_template, session, redirect, url_for, current_app, flash, request
from flask_login import login_required, current_user
from . import main
from .forms import PostForm, EditProfileForm, EditProfileAdminForm
from .. import db
from ..models import User, Role, Permission, Post
from ..email import send_email
from ..decorators import admin_required

##处理首页博客文章的路由
@main.route('/', methods=['GET', 'POST'])
def index():
	form = PostForm()
	if current_user.can(Permission.WRITE_ARTICLES) and \
			form.validate_on_submit():
		post = Post(body=form.body.data,
					author=current_user._get_current_object())   ###这里的current_user._get_current_object()的用法，是提取真正的对象   优点懵逼！！？
		db.session.add(post)
		return redirect(url_for('.index'))
	page = request.args.get('page', 1, type=int)
	pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
				page, per_page=current_app.config['FLASKY_PER_PAGE'],
				error_out=False)
				##error_out=False,当请求页数超出范围，则会返回404错误 
	posts = pagination.itmes
	return render_template('index.html', form=form, posts=posts, pagination=pagination)


#用户资料页面的路由。很好奇为什么放这里了，app/auth/views与app/main/views这两个添加路由.py有什么区别？
@main.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		abort(404)
	posts = user.posts.order_by(Post.timestamp.desc()).all() ##找当前用户的posts属性(对应Post类里面的所有博客
	return render_template('user.html', user=user, posts=posts)
	
	
##用户资料编辑路由
@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.name = form.name.data
		current_user.location = form.location.data
		current_user.about_me = form.about_me.data
		db.session.add(current_user)      ##一直很好奇为什么后面不加上db.session.commit() ??
		flash('您的个人资料已更新')
		return redirect(url_for('.user', username=current_user.username))
	form.username.data = current_user.username
	form.name.data = current_user.name
	form.location.data = current_user.location
	form.about_me.data = current_user.about_me
	return render_template('edit_profile.html', form=form)
	
###管理员的资料编辑路由
@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
	user = User.query.get_or_404(id)
	form = EditProfileAdminForm(user=user)
	if form.validate_on_submit():
		user.email = form.email.data
		user.username = form.username.data
		user.confirmed = form.confirmed.data
		user.role = Role.query.git(form.role.data)
		user.name = form.name.data
		user.location = form.location.data
		user.about_me = form.about_me.data
		db.session.add(user)
		flash('这些资料已更新')
		return redirect(url_for('.user', username=user.username))
	form.email.data = user.email
	form.username.data = user.username
	form.confirmed.data = user.confirmed
	form.role.data = user.role_id
	form.name.data = user.name
	form.location.data = user.location
	form.about_me.data = user.about_me
	return render_template('edit_profile.html', form=form, user=user)
		
