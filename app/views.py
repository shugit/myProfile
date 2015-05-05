from flask import render_template, flash, redirect, session, url_for, request, g
from datetime import datetime
from app import app, db
from models import *
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, EditProjectForm, EditFacilityForm, AddFacilityForm, AddProjectForm
import helper
import pprint


@app.route('/')
@app.route('/index')
def index():
    the_companies = Facility.query.filter_by(type='company').order_by(Facility.start_time).all()
    the_schools = Facility.query.filter_by(type='school').order_by(Facility.start_time).all()
    the_user = User.query.order_by(User.id).first()
    the_rewards = Reward.query.all()
    the_skills = Skill.query.all()
    the_publications = Publication.query.all()
    return render_template('index.html',
                           title='Home',
                           projects=helper.getProjects(),
                           companies=the_companies,
                           schools=the_schools,
                           user=the_user,
                           rewards=the_rewards,
                           skills=the_skills,
                           publications=the_publications
                           )
'''Project'''
'''Edit'''
@app.route('/project/<int:project_id>')
def project(project_id):
    project = Project.query.get(project_id)
    if project:
        return render_template('display/project.html',
                               project=project,
                               projects=helper.getProjects())
    else:
        flash("Project not found")
        return redirect(url_for('index'))


@app.route('/project/<int:project_id>/edit')
def edit_project_form(project_id):
    the_project = Project.query.get(project_id)
    form = EditProjectForm()
    form.set_choices()
    form.name.data = the_project.name
    form.description.data = the_project.description
    print form.facility.default
    if the_project.start_time is not None:
        form.start_time.data = the_project.start_time
    if the_project.end_time is not None:
        form.end_time.data = the_project.end_time
    return render_template('edit/project.html',
                           form=form,
                           projects=helper.getProjects())


@app.route('/project/<int:project_id>/edit', methods=['GET', 'POST'])
def edit_project(project_id):
    form = EditProjectForm(request.form)
    project = Project.query.get(project_id)
    form.set_choices()
    if form.validate_on_submit():
        project.name = form.name.data
        project.description = form.description.data
        project.start_time = form.start_time.data
        project.end_time = form.end_time.data
        project.facility = form.facility.data
        db.session.add(project)
        db.session.commit()
        flash('Your change is saved to project %s' % project.name)
        return redirect(url_for('project',
                                project_id=project.id))
    else:
        flash('Your change is not saved to project %s' % project.name)
    return render_template('edit/project.html',
                           form=form,
                           projects=helper.getProjects())

'''Add Project'''
@app.route('/project/add')
def add_project_form():
    form = AddProjectForm()
    form.set_choices()
    return render_template('add/project.html',
                           form=form,
                           projects=helper.getProjects())


@app.route('/project/add', methods=['GET', 'POST'])
def add_project():
    form = AddProjectForm(request.form)
    form.set_choices()
    if form.validate_on_submit():
        project = Project()
        project.name = form.name.data
        project.description = form.description.data
        project.start_time = form.start_time.data
        project.end_time = form.end_time.data
        project.facility = form.facility.data
        db.session.add(project)
        db.session.commit()
        flash('Your add is saved to project %s' % project.name)
        return redirect(url_for('project',
                                project_id=project.id))
    else:
        flash('Your add is not saved to project %s' % project.name)
    return render_template('edit/project.html',
                           form=form,
                           projects=helper.getProjects())


'''Facility'''
'''Edit'''

@app.route('/facility/<int:facility_id>/edit')
def edit_facility_form(facility_id):
    the_facility = Facility.query.get(facility_id)
    form = EditFacilityForm()
    form.name.data = the_facility.name
    form.position.data = the_facility.position
    form.location.data = the_facility.location
    if the_facility.start_time is not None:
        form.start_time.data = the_facility.start_time
    if the_facility.end_time is not None:
        form.end_time.data = the_facility.end_time
    form.set_projects_choices()
    form.type.data = '8'
    return render_template('edit/facility.html',
                           form=form,
                           projects=helper.getProjects())


@app.route('/facility/<int:facility_id>/edit', methods=['GET', 'POST'])
def edit_facility(facility_id):
    form = EditFacilityForm(request.form)
    facility = Facility.query.get(facility_id)
    if form.validate_on_submit():
        facility.name = form.name.data
        facility.start_time = form.start_time.data
        facility.end_time = form.end_time.data
        facility.location = form.location.data
        facility.position = form.position.data
        facility.type = 'school' if form.type.data == 1 else 'company'
        db.session.add(facility)
        db.session.commit()
        flash('Your change is saved to project %s' % facility.name)
        return redirect(url_for('index'))
    else:
        flash('Your change is not saved to project %s' % facility.name)
    return render_template('edit/facility.html',
                           form=form,
                           projects=helper.getProjects())


'''Add Facility'''
@app.route('/facility/add')
def add_facility_form():
    form = AddFacilityForm()
    form.set_projects_choices()
    return render_template('add/facility.html',
                           form=form,
                           projects=helper.getProjects())

@app.route('/facility/add', methods=['GET', 'POST'] )
def add_facility():
    form = AddFacilityForm()
    form.set_projects_choices()
    facility = Facility()
    if form.validate_on_submit():
        facility.name = form.name.data
        facility.start_time = form.start_time.data
        facility.end_time = form.end_time.data
        facility.location = form.location.data
        facility.position = form.position.data
        facility.type = 'school' if form.type.data == 1 else 'company'
        db.session.add(facility)
        db.session.commit()
        flash('Your change is saved to project %s' % facility.name)
        return redirect(url_for('index'))
    else:
        flash('Your change is not saved to project %s' % facility.name)
    return render_template('add/facility.html',
                           form=form,
                           projects=helper.getProjects())


"""
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        # login and validate the user...
        username = form.username
        password = form.password

        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

    """