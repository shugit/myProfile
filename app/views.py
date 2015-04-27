from flask import render_template, flash, redirect, session, url_for, request, g
from datetime import datetime
from app import app, db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/post/<int:post_id>')
def post():
    return render_template('post.html')