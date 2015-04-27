from flask import render_template, flash, redirect, session, url_for, request, g
from datetime import datetime
from app import app, db
from models import Project


@app.route('/')
@app.route('/index')
def index():
    projects = Project.query.all()
    return render_template('index.html',
                           title='Home',
                           projects=projects
                           )

@app.route('/post/<int:post_id>')
def post():
    return render_template('post.html')