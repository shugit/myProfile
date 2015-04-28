from flask import render_template, flash, redirect, session, url_for, request, g
from datetime import datetime
from app import app, db
from models import Project,Facility


@app.route('/')
@app.route('/index')
def index():
    projects = Project.query.all()
    companies = Facility.query.filter_by(type='company').all()
    schools = Facility.query.filter_by(type='school').all()
    return render_template('index.html',
                           title='Home',
                           projects=projects,
                           companies=companies,
                           schools=schools
                           )

@app.route('/project/<int:project_id>')
def project(project_id):

    projects = Project.query.all()
    project = Project.query.filter_by(id=project_id).first()
    if project:
        return render_template('project.html',
                           project=project,
                           projects=projects)
    else:
        flash("Project not found")
        return redirect(url_for('index'))