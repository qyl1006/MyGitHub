from . import db, login_manager
from werkzeug .security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request
from . import db
from datetime import datetime
import hashlib

#定义Role模型
class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	default = db.Column(db.Boolean, default=False, index=True)
	permissions = db.Column(db.Integer)
	##与User模型的关系  一对User
	users = db.relationship('User', backref='role', lazy='dynamic') #与User类相链接的桥梁
	
#在数据库中创建角色，使用了静态方法;True与False各为对应default的值	
	@staticmethod
	def insert_roles():
		roles = {
			'User': (Permission.FOLLOW | 
					 Permission.COMMENT | 
					 Permission.WRITE_ARTICLES, True),
			'Moderator': (Permission.FOLLOW | 
						  Permission.COMMENT | 
						  Permission.WRITE_ARTICLES | 
						  Permission.MODERATE_COMMENTS, False),
			'Administrator': (0xff, False)
		}
		for r in roles:
			role = Role.query.filter_by(name=r).first()
			if role is None:
				role = Role(name=r)
			role.permissions = roles[r][0]
			role.default = roles[r][1]
			db.session.add(role)
		db.session.commit()
	
	def __repr__(self):
		return '<Role %r>' % self.name
	
##定义文章博客Post模型
class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.Text)  #文章内容
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) #时间，距发布body多久
	##与User模型关系 多对User
	author_id = db.Column(db.Integer, db.ForeignKey('users.id'))	#外键，和users表相连  
	
##########################################################################	
#####以下。。使用ForgeryPy包生成大量的博客文章，用测试用

	@staticmethod  
	def generate_fake(count=100):
		from random import seed,randint  
		import forgery_py  
          
		seed()  
		user_count = User.query.count()        #这行是查询一共有生成了多少虚拟用户  
		for i in range(count):
			u = User.query.offset(randint(0,user_count-1)).first()  
			p = Post(body = forgery_py.lorem_ipsum.sentences(randint(1,3)),  
					timestamp = forgery_py.date.date(True),  
					author = u)            #这一行，将用户和所发的文章绑定了起来  
		db.session.add(p)  
		db.session.commit()  
#######################################################################
	
	def __repr__(self):
		return '<Post %r>' % self.body
	

##定义User模型	
class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	##与Role模型的关系 多对Role
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  #外键，与roles表相连
	confirmed = db.Column(db.Boolean, default=False)  #confirmed默认属性为False
	##与Post模型关系 一对Post
	posts = db.relationship('Post', backref='author', lazy='dynamic') #与Post类相连接的桥梁
	
	###用户个人信息字段
	name = db.Column(db.String(64))
	location = db.Column(db.String(64))
	about_me = db.Column(db.Text())
	member_since = db.Column(db.DateTime(), default=datetime.utcnow)
	last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
	
	###在User模型中加入密码散列，分别用于在注册用户和验证用户环节
	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')  ##密码只写属性

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)  #密码的散列值
		
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password) ##比较用户输入的密码与数据库里
																	##散列值，一致就返回True

#? 不知道对不对！！加载用户的回调函数
	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))
		
	
		

###确认用户帐号
    #加密签名,返回令牌,有效期1h
	def generate_confirmation_token(self, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expiration)
		return s.dumps({'confirm': self.id})
		
	#验证令牌，并判定令牌id与current_user.id是否一致，通过就把confirmed属性设为True
	def confirm(self, token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token)  ##? 不明白token为什么是令牌字符串！？哪里有赋值？
		except:
			return False
		if data.get('confirm') != self.id:
			return False
		self.confirmed = True
		db.session.add(self)
		return True
	
	###定义默认的用户角色，
	def __init__(self, **kwargs):
		super(User, self).__init__(**kwargs)
		if self.role is None:
			if self.email == current_app.config['FLASKY_ADMIN']:
				self.role = Role.query.filter_by(permissions=0xff).first()
			if self.role is None:
				self.role = Role.query.filter_by(default=True).first()
	
	###检查用户是否有指定的权限
	def can(self, permissions):
		return self.role is not None and \
			(self.role.permissions & permissions) == permissions
			
	def is_administrator(self):
		return self.can(Permission.ADMINISTER)
		
	###刷新用户的最后访问时间
	def ping(self):
		self.last_seen = datetime.utcnow()
		db.session.add(self)	
	
	####生成Gravatar URL 一个头像服务网站的URL，通过计算每个邮箱地址的MD5散列值.
	def gravatar(self, size=100, default='idention', rating='g'):
		if request.is_secure:  ###判断request是否为https 
			url = 'https://secure.gravatar.com/acatar'
		else:
			url = 'http://www.gravatar.com/avatar'
		hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()
		return '{url}/{hash}?s={size}&d={default}&r=[rating]'.format(
			url=url, hash=hash, size=size, default=default, rating=rating)
			
#####################################################################
###以下。。使用ForgeryPy包生成大量的虚拟用户和，用测试用
	@staticmethod
	def generate_fake(count=100):
		from sqlalchemy.exc import IntegrityError
		from random import seed
		import forgery_py
		
		seed()
		for i in range(count):
			u = User(email=forgery_py.internet.email_address(),
					 username=forgery_py.internet.user_name(True),
					 password=forgery_py.lorem_ipsum.word(),
					 confirmed=True,
					 name=forgery_py.name.full_name(),
					 location=forgery_py.address.city(),
					 about_me=forgery_py.lorem_ipsum.sentence(),
					 member_since=forgery_py.date.date(True))
			db.session.add(u)
			try:
				db.session.commit()
			except IntegrityError:
				db.session.rollback()  ##异常就回滚
##################################################################			
	
	def __repr__(self):
		return '<User %r>' % self.username

##定义一个AnonymousUser类，
##将login_manager.anonymous_user设为AnonymousUser类对象，实际上就是未登录状态的current_user 
class AnonymousUser(AnonymousUserMixin):
	def can(self, permissions):
		return False
		
	def is_administrator(self):
		return False
login_manager.anonymous_user = AnonymousUser
		
#权限常量,权限类
class Permission:
	FOLLOW = 0x01
	COMMENT = 0x02
	WRITE_ARTICLES = 0x04
	MODERATE_COMMENTS = 0x08
	ADMINISTER = 0x80

	
