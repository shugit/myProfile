from flask import render_template, flash, redirect, session, url_for, request, g
from datetime import datetime
from app import app, db
from models import Project,Facility, User
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    projects = Project.query.all()
    companies = Facility.query.filter_by(type='company').all() # add order by
    schools = Facility.query.filter_by(type='school').all()  # add order by
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