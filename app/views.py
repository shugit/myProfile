from flask import render_template, flash, redirect, session, url_for, request, g
from datetime import datetime
from app import app, db
from models import *
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, ProjectForm, FacilityForm, SkillForm, RewardForm
import helper
import pprint


@app.route('/')
@app.route('/index')
def index():
    the_companies = Facility.query.filter_by(type='company').order_by(Facility.start_time.desc()).all()
    the_schools = Facility.query.filter_by(type='school').order_by(Facility.start_time.desc()).all()
    the_user = User.query.order_by(User.id).first()
    the_rewards = Reward.query.all()
    the_skills = Skill.query.order_by(Skill.scale.desc()).all()
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
'''View'''
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

'''Edit/Add Project '''
@app.route('/project/<path:action>/<int:project_id>')
def project_form(action='add', project_id=None):
    form = ProjectForm()
    form.set_choices()
    title ='Add Project'
    if action.lower() == 'add':
        pass
    elif action.lower() == 'edit':
        if project_id is None:
            flash("project id should not be empty")
            return redirect(url_for('404'))
        title = 'Edit Project'
        the_project = Project.query.get(project_id)
        form.name.data = the_project.name
        form.description.data = the_project.description
        form.facility.default = the_project.id
        if the_project.start_time is not None:
            form.start_time.data = the_project.start_time
        if the_project.end_time is not None:
            form.end_time.data = the_project.end_time
    else:
        flash("Action not foundL %s" % action)
        return redirect(url_for('index'))
    return render_template('edit/project.html',
                           form=form,
                           title=title,
                           projects=helper.getProjects())


@app.route('/project/<path:action>/<int:project_id>', methods=['GET', 'POST'])
def project_submit(action='add', project_id=None):
    form = ProjectForm(request.form)
    form.set_choices()
    title = 'Add Project Request Submitted'
    project = Project()
    if action.lower() == 'add':
        pass
    elif action.lower() == 'edit':
        if project_id is None:
            flash("project id should not be empty")
            return redirect(url_for('404'))
        title = 'Edit Project Request Submitted'
        project = Project.query.get(project_id)
    else:
        flash("Action not found: %s" % action)
        return redirect(url_for('index'))
    if form.validate_on_submit():
        project.name = form.name.data
        project.description = form.description.data
        project.start_time = form.start_time.data
        project.end_time = form.end_time.data
        project.facility = form.facility.data
        db.session.add(project)
        db.session.commit()
        flash('Your change is saved to project %s with id %d' % (project.name, project.id))
        return redirect(url_for('project',
                                project_id=project.id))
    else:
        flash('Your change is not saved to project %s with id %d' % (project.name, project.id))

    return render_template('edit/project.html',
                           form=form,
                           title=title,
                           projects=helper.getProjects())


'''Facility'''
'''View'''


'''Edit/Add Facility'''
@app.route('/facility/<path:action>/<int:facility_id>')
def facility_form(action='add', facility_id=None):
    form = FacilityForm()
    form.set_projects_choices()
    form.type.data = '8'
    title = 'Add Facility'
    if action.lower() == 'add':
        pass
    elif action.lower() == 'edit':
        if facility_id is None:
            flash("facility id should not be empty")
            return redirect(url_for('404'))
        title = 'Edit Facility'
        the_facility = Facility.query.get(facility_id)
        form.name.data = the_facility.name
        form.position.data = the_facility.position
        form.location.data = the_facility.location
        if the_facility.start_time is not None:
            form.start_time.data = the_facility.start_time
        if the_facility.end_time is not None:
            form.end_time.data = the_facility.end_time
    else:
        flash("Action not found: %s" % action)
        return redirect(url_for('index'))
    return render_template('edit/facility.html',
                           title=title,
                           form=form,
                           projects=helper.getProjects())


@app.route('/facility/<path:action>/<int:facility_id>', methods=['GET', 'POST'])
def facility_submit(action='add', facility_id=None):
    form = FacilityForm(request.form)
    facility = Facility()
    if action.lower() == 'add':
        pass
    elif action.lower() == 'edit':
        if facility_id is None:
            flash("facility id should not be empty")
            return redirect(url_for('404'))
        facility = Facility.query.get(facility_id)
    else:
        flash("Action not found: %s" % action)
        return redirect(url_for('index'))
    if form.validate_on_submit():
        facility.name = form.name.data
        facility.start_time = form.start_time.data
        facility.end_time = form.end_time.data
        facility.location = form.location.data
        facility.position = form.position.data
        facility.type = 'school' if form.type.data == 1 else 'company'
        db.session.add(facility)
        db.session.commit()
        flash('Your change is saved to facility %s with id %d' % (facility.name, facility.id))
        return redirect(url_for('index'))
    else:
        flash('Your change is not saved to facility %s with id %d' % (facility.name, facility.id))
    return render_template('edit/facility.html',
                           form=form,
                           projects=helper.getProjects())



'''Skill'''
'''View'''

'''Edit/Add Skill'''
@app.route('/skill/<path:action>/<int:skill_id>')
def skill_form(action='add', skill_id=None):
    form = SkillForm()
    title = 'Add Skill'
    if action.lower() == 'add':
        pass
    elif action.lower() == 'edit':
        if skill_id is None:
            flash("skill id should not be empty")
            return redirect(url_for('404'))
        title = 'Edit Skill'
        the_object = Skill.query.get(skill_id)
        form.name.data = the_object.name
        form.description.data = the_object.description
        form.scale.data = the_object.scale
    else:
        flash("Action not found: %s" % action)
        return redirect(url_for('index'))
    return render_template('edit/skill.html',
                           title=title,
                           form=form,
                           projects=helper.getProjects())


@app.route('/skill/<path:action>/<int:skill_id>', methods=['GET', 'POST'])
def skill_submit(action='add', skill_id=None):
    form = SkillForm(request.form)
    the_object = Skill()
    title = 'Add Skill Submitted'
    if action.lower() == 'add':
        pass
    elif action.lower() == 'edit':
        if skill_id is None:
            flash("skill id should not be empty")
            return redirect(url_for('404'))
        the_object = Skill.query.get(skill_id)
        title = 'Edit Skill Submitted'
    else:
        flash("Action not found: %s" % action)
        return redirect(url_for('index'))
    if form.validate_on_submit():
        the_object.name = form.name.data
        the_object.description = form.description.data
        the_object.scale = form.scale.data
        db.session.add(the_object)
        db.session.commit()
        flash('Your change is saved to skill %s with id %d' % (the_object.name, the_object.id))
        return redirect(url_for('index'))
    else:
        flash('Your change is not saved to skill %s with id %d' % (the_object.name, the_object.id))
    return render_template('edit/skill.html',
                           form=form,
                           title=title,
                           projects=helper.getProjects())

'''Reward'''
'''View'''

'''Edit/Add Reward'''
@app.route('/reward/<path:action>/<int:reward_id>')
def reward_form(action='add', reward_id=None):
    form = RewardForm()
    title = 'Add Reward'
    if action.lower() == 'add':
        pass
    elif action.lower() == 'edit':
        if reward_id is None:
            flash("reward id should not be empty")
            return redirect(url_for('404'))
        title = 'Edit Reward'
        the_object = Reward.query.get(reward_id)
        form.name.data = the_object.name
        form.description.data = the_object.description
        form.scale.data = the_object.scale
    else:
        flash("Action not found: %s" % action)
        return redirect(url_for('index'))
    return render_template('edit/reward.html',
                           title=title,
                           form=form,
                           projects=helper.getProjects())


@app.route('/reward/<path:action>/<int:reward_id>', methods=['GET', 'POST'])
def reward_submit(action='add', reward_id=None):
    form = RewardForm(request.form)
    the_object = Reward()
    title = 'Add Reward Submitted'
    if action.lower() == 'add':
        pass
    elif action.lower() == 'edit':
        if reward_id is None:
            flash("reward id should not be empty")
            return redirect(url_for('404'))
        the_object = Reward.query.get(reward_id)
        title = 'Edit Reward Submitted'
    else:
        flash("Action not found: %s" % action)
        return redirect(url_for('index'))
    if form.validate_on_submit():
        the_object.name = form.name.data
        the_object.description = form.description.data
        db.session.add(the_object)
        db.session.commit()
        flash('Your change is saved to reward %s with id %d' % (the_object.name, the_object.id))
        return redirect(url_for('index'))
    else:
        flash('Your change is not saved to reward %s with id %d' % (the_object.name, the_object.id))
    return render_template('edit/reward.html',
                           form=form,
                           title=title,
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