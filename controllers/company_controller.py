from flask import Flask, render_template, request, redirect, Blueprint

from models.category import Category
from models.company import Company
from models.account import Account
from datetime import datetime

import repositories.company_repository as company_repository
import repositories.category_repository as category_repository
import repositories.account_repository as account_repository
import repositories.user_repository as user_repository


companys_blueprint = Blueprint("companys", __name__)


#INDEX
@companys_blueprint.route('/')
def company():
  category = category_repository.select_all()
  company = company_repository.select_all()
  account = account_repository.select_all()
  users = user_repository.select_all()
  return render_template('index.html', all_company=company, all_category=category, accounts=account, users=users)

# Create
@companys_blueprint.route('/', methods=['POST'])
def create_company():
  import datetime
  name = request.form['name']
  amount = request.form['amount']
  category = category_repository.select(request.form['category_id'])
  account = account_repository.select(request.form['account_id'])
  today = datetime.date.today()
  add_company = Company(name, amount, category, account, today)
  company_repository.save(add_company)
  account.amount -= float(amount)
  account_repository.update(account)
  return redirect('/')

# Edit
@companys_blueprint.route("/companys/<id>/edit")
def edit_company(id):
  company = company_repository.select(id)
  category = category_repository.select_all()
  account = account_repository.select_all()
  return render_template('companys/edit.html', company=company, all_category=category, accounts=account)

# Update
@companys_blueprint.route("/companys/<id>", methods=['POST'])
def update_company(id):
  name = request.form["name"]
  amount = request.form["amount"]
  category = category_repository.select(request.form['category_id'])
  account = account_repository.select(request.form['account_id'])
  update_company = Company(name, amount, category, account, id)
  company_repository.update(update_company)
  account.amount += float(amount)
  account_repository.update(account)
  return redirect("/") 

# Delete
@companys_blueprint.route("/companys/<id>/delete", methods=["POST"])
def delete_company(id):
  company_repository.delete(id)
  return redirect("/")