from db.run_sql import run_sql

from models.company import Company
from models.category import Category
from models.user import User

import repositories.user_repository as user_repository
import repositories.company_repository as company_repository 
import repositories.category_repository as category_repository

def save(company):
  sql = "INSERT INTO companys (name, amount, category_id, user_id) VALUES (%s, %s, %s) RETURNING id"
  values = [company.name, company.amount, company.category.id, company.user.id]
  results = run_sql(sql, values)
  company.id = results[0]['id']

def select_all():
  companys = []

  sql = "SELECT * FROM companys"
  results = run_sql(sql)
  for row in results:
    category = category_repository.select(row['category_id'])
    user = user_repository.selcet(row['user_id'])
    company = Company(row['name'], row['amount'], category, user, row['id'])
    companys.append(company)
  return companys

def select(id):
  company = None
  sql = "SELECT * FROM companys WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]

  if result is not None:
    category = category_repository.select(result['category_id'])
    user = user_repository.select(result['user_id'])
    company = Company(result['name'], result['amount'], category, user, result['id'])
  return company

def delete_all():
  sql = "DELETE FROM companys"
  run_sql(sql)

def delete(id):
  sql = "DELETE FROM companys WHERE id = %s"
  values = [id]
  run_sql(sql, values)

def update(company):
  sql = "UPDATE companys SET (name, amount, category_id, user_id) = (%s, %s, %s, %s) WHERE id = %s"
  values = [company.name, company.amount, company.category.id, company.user.id, company.id]
  run_sql(sql, values)