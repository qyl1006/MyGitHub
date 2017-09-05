from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
class NameForm(Form):
	name = StringField('你叫什么名字?', validators=[Required()])
	submit = SubmitField('确认')
