from db.run_sql import run_sql

from models.account import Account

import repositories.account_repository as account_repository


def save(account):
  sql = "INSERT INTO accounts (account_name, amount) VALUES (%s, %s) RETURNING id"
  values = [account.account_name, account.amount]
  results = run_sql(sql, values)
  account.id = results[0]['id']
  return account

def select_all():
  accounts = []

  sql = "SELECT * FROM accounts"
  results = run_sql(sql)
  for row in results:
    account = Account(row['account_name'], row['amount'], row['id'])
    accounts.append(account)
  return accounts

def select(id):
  account = None
  sql = "SELECT * FROM accounts WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]

  if result is not None:
    account = Account(result['account_name'], result['amount'], result['id'])
  return account

def delete_all():
  sql = "DELETE FROM accounts"
  run_sql(sql)

def delete(id):
  sql = "DELETE FROM accounts WHERE id = %s"
  values = [id]
  run_sql(sql, values)

def update(account):
  sql = "UPDATE accounts SET (account_name, amount) = (%s, %s) WHERE id = %s"
  values = [account.account_name, account.amount]
  run_sql(sql, values)