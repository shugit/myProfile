from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class EditProjectForm(Form):
    name = StringField('name',validators=[DataRequired(),Length(min=1,max=140)])
    description = StringField('description', validators=[DataRequired()])
