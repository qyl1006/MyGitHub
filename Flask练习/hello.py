from flask import Flask, render_template, session, redirect, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

#@app.route('/')
#def index():
    #return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
	
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

#定义一个表单类，参数validators指定验证函数Required()，Submit提交按钮
class NameForm(Form):
	name = StringField('你叫什么名字?', validators=[Required()])
	submit = SubmitField('确认')

#表单的路由方法，validate_on_submit()调用name上的Required()，为True用户输入的就通过
#data属性获取，然后清空表单字段form.name.data；最后(为False直接)渲染表单模块,	
@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'), 
							current_time=datetime.utcnow())

if __name__ == '__main__':
    manager.run()
