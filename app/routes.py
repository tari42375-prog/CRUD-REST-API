from app import app
from flask import request
from app.controller import UserController

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return UserController.store()
    else:
        return UserController.index()

@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)
