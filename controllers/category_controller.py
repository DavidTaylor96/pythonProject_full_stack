from flask import Flask, render_template, request, redirect, Blueprint
from models.category import Category
import repositories.category_repository as category_repository


categorys_blueprint = Blueprint("categorys", __name__)


# INDEX
@categorys_blueprint.route('/categorys')
def users():
  categorys = category_repository.select_all()
  return render_template("categorys/index.html", categorys=categorys)

# #New
@categorys_blueprint.route('/categorys/new', methods=["GET"])
def new_user():
  categorys = category_repository.select_all()
  return render_template("categorys/index.html", categorys=categorys)

#Create
@categorys_blueprint.route('/categorys', methods=['POST'])
def create_user():
  name = request.form["name"]
  new_category = User(name)
  category_repository.save(new_category)
  return redirect('/categorys')
