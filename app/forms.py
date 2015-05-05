from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, DateField, SelectField,TextAreaField, SelectMultipleField
from wtforms.ext.appengine.fields import ReferencePropertyField
from wtforms.validators import DataRequired, Length
from models import Facility, Project
from app import app
import datetime


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    def validate_username(self):
        return 'unknow'

class EditProjectForm(Form):
    name = StringField('name',validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    start_time = DateField('start time', format=app.config.get('DATE_FORMAT'),default=datetime.datetime.now())
    end_time = DateField('end time', format=app.config.get('DATE_FORMAT'),default=datetime.datetime.now())
    facility = SelectField('facility', coerce=int)

    def set_choices(self):
        facility_list = Facility.query.order_by(Facility.start_time).all()
        choices = []
        for facility in facility_list:
            choices.append([facility.id, facility.name])
        self.facility.choices = choices


class EditFacilityForm(Form):
    name = StringField('name',validators=[DataRequired(),Length(min=1,max=140)])
    start_time = DateField('start time', validators=[], format=app.config.get('DATE_FORMAT'),default=datetime.datetime.now())
    end_time = DateField('end time',validators=[], format=app.config.get('DATE_FORMAT'),default=datetime.datetime.now())
    position = StringField('position')
    location = StringField('location')
    type = SelectField('type', choices=[(1,'School'),(2,'Company')],coerce=int)
    projects = SelectMultipleField('projects')

    def set_projects_choices(self):
        choices = []
        for project in Project.query.all():
            choices.append([project.id,project.name])
        self.projects.choices = choices


class AddFacilityForm(Form):
    name = StringField('name',validators=[DataRequired(),Length(min=1,max=140)])
    start_time = DateField('start time', validators=[], format=app.config.get('DATE_FORMAT'),default=datetime.datetime.now())
    end_time = DateField('end time',validators=[], format=app.config.get('DATE_FORMAT'),default=datetime.datetime.now())
    position = StringField('position')
    location = StringField('location')
    type = SelectField('type', choices=[(1,'School'),(2,'Company')],coerce=int)
    projects = SelectMultipleField('projects')

    def set_projects_choices(self):
        choices = []
        for project in Project.query.all():
            choices.append([project.id,project.name])
        self.projects.choices = choices


class AddProjectForm(Form):
    name = StringField('name',validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    start_time = DateField('start time', format=app.config.get('DATE_FORMAT'),default=datetime.datetime.now())
    end_time = DateField('end time', format=app.config.get('DATE_FORMAT'),default=datetime.datetime.now())
    facility = SelectField('facility', coerce=int)

    def set_choices(self):
        facility_list = Facility.query.order_by(Facility.start_time).all()
        choices = []
        for facility in facility_list:
            choices.append([facility.id, facility.name])
        self.facility.choices = choices
