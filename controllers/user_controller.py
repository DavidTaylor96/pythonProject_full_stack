from flask import Flask, render_template, request, redirect, Blueprint
from models.user import User
import repositories.user_repository as user_repository


users_blueprint = Blueprint("users", __name__)


# INDEX
@users_blueprint.route('/users')
def users():
  users = user_repository.select_all()
  return render_template("users/index.html", users=users)

# #New
@users_blueprint.route('/users/new')
def new_user():
  users = user_repository.select_all()
  return render_template("users/new.html", users=users)

#Create
@users_blueprint.route('/users', methods=['POST'])
def create_user():
  name = request.form["username"]
  amount = request.form["amount"]
  new_user = User(name, amount)
  user_repository.save(new_user)
  return redirect('/users')

# Edit
@users_blueprint.route("/users/<id>/edit")
def edit_user(id):
  user = user_repository.select(id)
  return render_template('users/edit.html', user=user)

# Update
@user_repository.route("/users/<id>", methods=['POST'])
def update_user