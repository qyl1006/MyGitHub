from . import db, login_manager
from werkzeug .security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db
from datetime import datetime

#定义Role和User模型
class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	default = db.Column(db.Boolean, default=False, index=True)
	permissions = db.Column(db.Integer)
	users = db.relationship('User', backref='role', lazy='dynamic')
	
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
		
class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	rold_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	confirmed = db.Column(db.Boolean, default=False)  #confirmed默认属性为False
	
	###用户个人信息字段
	name = db.Column(db.String(64))
	location = db.Column(db.String(64))
	about_me = db.Column(db.Text())
	member_since = db.Column(db.DateTime(), default=datetime.utcnow)
	last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
	
	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
		
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

#? 不知道对不对
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

	
