from db.run_sql import run_sql
from models.user import User


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

def select_id(id):
  user = None
  sql = "SELECT * FROM users WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]

  if result is not None:
    user= User(result['name'], result['amount'], result['id'])
  return user

def delete_all():
  sql = "DELETE FROM users"
  run_sql(sql)