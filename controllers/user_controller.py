# from flask import Flask, render_template, request, redirect, Blueprint
# from models.user import User
# import repositories.user_repository as user_repository


# users_blueprint = Blueprint("users", __name__)

# @users_blueprint.route('/')
# def users():
#   users = user_repository.select_all()
#   return render_template("index.html", users=users)