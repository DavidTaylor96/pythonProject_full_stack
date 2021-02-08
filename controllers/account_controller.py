from flask import Flask, render_template, request, redirect, Blueprint
from models.account import Account
import repositories.account_repository as account_repository


account_blueprint = Blueprint("account", __name__)

#New
@account_blueprint.route('/accounts/new')
def new_user():
  accounts = account_repository.select_all()
  return render_template("accounts/new.html", accounts=accounts)

#Create
@account_blueprint.route('/accounts', methods=['POST'])
def create_user():
  name = request.form["account_name"]
  amount = request.form["amount"]
  new_account = Account(name, amount)
  account_repository.save(new_account)
  return redirect('/')

# Edit
@account_blueprint.route("/accounts/<id>/edit")
def edit_account(id):
  account = account_repository.select(id)
  return render_template('accounts/edit.html', account=account)

# Update
@account_blueprint.route("/accounts/<id>", methods=['POST'])
def update_account(id):
  name = request.form["account_name"]
  amount = request.form['amount']
  updated_account = Account(name, amount, id)
  account_repository.update(updated_account)
  return redirect("/")

# Delete
@account_blueprint.route("/accounts/<id>/delete", methods=["POST"])
def delete_account(id):
  account_repository.delete(id)
  return redirect("/")