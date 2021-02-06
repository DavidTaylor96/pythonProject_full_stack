from flask import Flask, render_template, request, redirect, Blueprint

from models.category import Category
from models.company import Company

import repositories.company_repository as company_repository
import repositories.category_repository as category_repository


companys_blueprint = Blueprint("companys", __name__)


#INDEX
@companys_blueprint.route('/companys')
def company():
  companys = company_repository.select_all()
  return render_template('companys/index.html', companys=companys)

# New
@companys_blueprint.route('/companys/new', methods=['GET'])
def new_company():
  companys = company_repository.select_all()
  return render_template('companys/new.html', companys=companys)

# Create
@companys_blueprint.route('/companys', methods=['POST'])
def create_company():
  name = request.form['name']
  amount = request.form['amount']
  category_id = category_repository.select(id)
  new_company = Company(name, amount, category_id)
  company_repository.save(new_company)
  return redirect('/companys')


# # Edit
# @companys_blueprint.route("/companys/<id>/edit")
# def edit_company(id):
#   company = company_repository.select(id)
#   return render_template('companys/edit.html', company=company)

# # Update
# @companys_blueprint.route("/companys/<id>", methods=['POST'])
# def update_company(id):
#   name = request.form["username"]
#   amount = request.form["amount"]
#   updated_company = Company(name, amount, id)
#   company_repository.update(updated_company)
#   return redirect("/companys")

# # Delete
# @companys_blueprint.route("/companys/<id>/delete", methods=["POST"])
# def delete_company(id):
#   company_repository.delete(id)
#   return redirect("/companys")