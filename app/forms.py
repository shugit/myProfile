from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, DateField, SelectField
from wtforms.validators import DataRequired, Length
from models import Facility
from app import app

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    def validate_username(self):
        return 'unknow'

class EditProjectForm(Form):
    name = StringField('name',validators=[DataRequired(),Length(min=1,max=140)])
    description = StringField('description', validators=[DataRequired()])
    start_time = DateField('start time', validators=[], format=app.config.get('DATE_FORMAT'))
    end_time = DateField('end time',validators=[], format=app.config.get('DATE_FORMAT'))
    facility = SelectField('Facility')
    def set_choices(self):
        from models import Facility
        fs = Facility.query.order_by(Facility.start_time).all()
        self.facility.choices = fs
        print fs

class EditFacilityForm(Form):
    name = StringField('name',validators=[DataRequired(),Length(min=1,max=140)])
    description = StringField('description', validators=[DataRequired()])
    start_time = DateField('start_time', validators=[], format=app.config.get('DATE_FORMAT'))
    end_time = DateField('end_time',validators=[], format=app.config.get('DATE_FORMAT'))


