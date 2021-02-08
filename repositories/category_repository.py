from db.run_sql import run_sql

from models.category import Category
from models.company import Company

import repositories.company_repository as company_repository
import repositories.category_repository as category_repository

def save(category):
  sql = "INSERT INTO categorys ( name ) VALUES ( %s ) RETURNING id"
  values = [category.name]
  results = run_sql(sql, values)
  category.id = results[0]['id']


def select_all():
  categorys = []

  sql = "SELECT * FROM categorys"
  results = run_sql(sql)
  for row in results:
      category = Category(row['name'], row['id'])
      categorys.append(category)
  return categorys

def select(id):
  category = None
  sql = "SELECT * FROM categorys WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]

  if result is not None:
    category = Category(result['name'], result['id'])
  return category


def delete_all():
  sql = "DELETE FROM categorys "
  run_sql(sql)


def delete(id):
  sql = "DELETE FROM categorys WHERE id = %s"
  values = [id]
  run_sql(sql, values)

# def companys(category):
#   companys = []
  
#   sql = "SELECT * FROM companys WHERE category_id = %s"
#   values = [category.id]
#   results = run_sql(sql, values)

#   for row in results:
#     company = Company(row['name'], row['amount'], row['category_id'], row['id'])
#     companys.append(company)
#   return companys