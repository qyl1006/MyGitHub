from datetime import datetime  #关于渲染时间的一个变量
from flask import render_template, session, redirect, url_for, current_app, flash
from flask_login import login_required, current_user
from . import main
from .forms import NameForm, EditProfileForm, EditProfileAdminForm
from .. import db
from ..models import User, Role
from ..email import send_email


#表单的路由方法，validate_on_submit()调用name上的Required()，为True用户输入的就通过
#data属性获取，然后清空表单字段form.name.data；最后(为False直接)渲染表单模块,	
@main.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		#old_name = session.get('name')
		#if old_name is not None and old_name != form.name.data:
		    #flash('看起来你已经更换之前的名字！')
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username=form.name.data)
			db.session.add(user)
			session['known'] = False
#若定义了管理员邮箱——True	#发送邮箱实例，#每当输入新的name就自动发邮件给管理员	
 ##mail/new_user 在templates下面子文件夹mail里面,调用名字为new_user的txt和html文件,
 ##网上看的，不知道对不对？	
			if current_app.config['FLASKY_ADMIN']:  
				send_email(app.config['FLASKY_ADMIN'], 'New User', 
							'mail/new_user', user=user)
		else:
			session['known'] = True    
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('.index'))
	return render_template('index.html', form=form, name=session.get('name'),
							known=session.get('known', False), 
							current_time=datetime.utcnow())


#用户资料页面的路由。很好奇为什么放这里了，app/auth/views与app/main/views这两个添加路由.py有什么区别？
@main.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		abort(404)
	return render_template('user.html', user=user)
	
##用户资料编辑路由
@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		current_user.name = form.name.data
		current_user.location = form.location.data
		current_user.about_me = form.about_me.data
		db.session.add(current_user)      ##一直很好奇为什么后面不加上db.session.commit() ??
		flash('您的个人资料已更新')
		return redirect(url_for('.user', username=current_user.username))
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
		
