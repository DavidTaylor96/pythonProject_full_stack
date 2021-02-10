from db.run_sql import run_sql

from models.user import User

import repositories.user_repository as user_repository


def save(user):
  sql = "INSERT INTO users(full_name) VALUES (%s) RETURNING id"
  values = [user.full_name]
  results = run_sql(sql, values)
  user.id = results[0]['id']
  return user


def select_all():
  users = []

  sql = "SELECT * FROM users"
  results = run_sql(sql)
  for row in results:
    user = User(row['full_name'], row['id'])
    users.append(user)
  return users

def select(id):
  sql = "SELECT * FROM users WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]
  user = User(result['full_name'], result['id'])
  return user


def delete_all():
  sql = "DELETE FROM users"
  run_sql(sql)

def delete(id):
  sql = "DELETE FROM users WHERE id = %s"
  values = [id]
  run_sql(sql, values)

def update(user):
  sql = "UPDATE users SET full_name = %s WHERE id = %s"
  values = [user.full_name, user.id]
  run_sql(sql, values)