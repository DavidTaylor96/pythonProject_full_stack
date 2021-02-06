from db.run_sql import run_sql
from models.user import User
from models.category import Category
from models.company import Company

def save(user):
  sql = "INSERT INTO users(full_name, amount) VALUES (%s, %s) RETURNING id"
  values = [user.full_name, user.amount]
  results = run_sql(sql, values)
  user.id = results[0]['id']
  return user


def select_all():
  users = []

  sql = "SELECT * FROM users"
  results = run_sql(sql)
  for row in results:
    user = User(row['full_name'], row['amount'], row['id'])
    users.append(user)
  return users

def select(id):
  sql = "SELECT * FROM users WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]
  user = User(result['full_name'], result['amount'], result['id'])
  return user


def delete_all():
  sql = "DELETE FROM users"
  run_sql(sql)

def delete(id):
  sql = "DELETE FROM users WHERE id = %s"
  values = [id]
  run_sql(sql, values)

def update(user):
  sql = "UPDATE users SET (full_name, amount) = (%s, %s) WHERE id = %s"
  values = [user.full_name, user.amount, user.id]
  run_sql(sql, values)