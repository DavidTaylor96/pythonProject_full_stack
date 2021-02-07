from flask import Flask, render_template, request, redirect, Blueprint

from models.category import Category
from models.company import Company

import repositories.company_repository as company_repository
import repositories.category_repository as category_repository


companys_blueprint = Blueprint("companys", __name__)


#INDEX
@companys_blueprint.route('/')
def company():
  company = company_repository.select_all()
  return render_template('index.html', all_company=company)

# New
@companys_blueprint.route('/')
def new_company():
  category = category_repository.select_all()
  return render_template('index.html', all_category=category)

# Create
@companys_blueprint.route('/', methods=['POST'])
def create_company():
  name = request.form['name']
  amount = request.form['amount']
  category_id = request.form['category_id']
  create_company = Company(name, amount, category_id)
  company_repository.save(create_company)
  return redirect('/')


# Edit
@companys_blueprint.route("/companys/<id>/edit")
def edit_company(id):
  company = company_repository.select(id)
  return render_template('companys/edit.html', company=company)

# Update
@companys_blueprint.route("/companys/<id>", methods=['POST'])
def update_company(id):
  name = request.form["name"]
  amount = request.form["amount"]
  category = request.form['category_id']
  update_company = Company(name, amount, category)
  company_repository.update(update_company)
  return redirect("/") 

# Delete
@companys_blueprint.route("/companys/<id>/delete", methods=["POST"])
def delete_company(id):
  company_repository.delete(id)
  return redirect("/")