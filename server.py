#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from postboard import Database

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is the home page.'

@app.route('/hello')
def welcome():
    return 'Hello!'

@app.route('/hello/<username>')
def hello_sb(username):
    return 'Hello, %s!' % username

@app.route('/user')
def user():
    return 'This is a user page.'

@app.route('/user/<username>')
def user_sb(username):
    return 'This is %s\'s user page.' % username

@app.route('/postboard', methods=['GET', 'POST'])
def visit_postboard():
    database = Database('post.db')
    if request.method == 'POST':
        database.addEntry(request.form['content'])
    posts = database.showDatabase() # posts is a list of tuple.
    return render_template('postboard.html', posts=posts)

@app.route('/delete')
def delete():
    database = Database('post.db')
    database.deleteEntry(request.args['id'])
    return redirect(url_for('visit_postboard'))

if __name__ == '__main__':
    app.run()
