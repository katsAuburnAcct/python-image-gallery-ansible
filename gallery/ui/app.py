import sys
sys.path.append('/home/ec2-user/python-image-gallery/gallery/ui')

from flask import Flask, request, render_template
from user_admin import setupDBConnection
from db import getUsers, addUser, editUser, deleteUser

app = Flask(__name__)

setupDBConnection()

@app.route('/admin')
def admin():
    users = getUsers()
    return render_template('admin.html', users= users)

@app.route('/admin/create')
def createUserRoute():
    return render_template('createUser.html')

@app.route('/admin/edit/<username>')
def editUserRoute(username):
    return render_template('editUser.html', username= username)

@app.route('/admin/delete/<username>')
def deleteUserRoute(username):
    return render_template('deleteUser.html', username= username)


@app.route('/create-user', methods=['POST'])
def onCreateUser():
    if request.method == 'POST':
        addUser(request.form['username'].rstrip(), request.form['password'].rstrip(), request.form['fullName'].rstrip())
    users = getUsers()
    return render_template('admin.html', users= users)

@app.route('/edit-user', methods=['POST'])
def onEditUser():
    if request.method == 'POST':
        editUser(request.form['username'].rstrip(), request.form['password'].rstrip(), request.form['fullName'].rstrip())
    users = getUsers()
    return render_template('admin.html', users= users)

@app.route('/delete-user/<username>')
def onDeleteUser(username):
    deleteUser(username.rstrip())
    users = getUsers()
    return render_template('admin.html', users= users)
