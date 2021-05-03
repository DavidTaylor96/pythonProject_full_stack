import pdb

from models.category import Category
from models.company import Company
from models.user import User 
from models.account import Account

import repositories.category_repository as category_repository
import repositories.company_repository as company_repository
import repositories.user_repository as user_repository
import repositories.account_repository as account_repository


account_repository.delete_all()
user_repository.delete_all()
category_repository.delete_all()
company_repository.delete_all()

user1 = User("David Taylor", 137)
user_repository.save(user1)

category1 = Category("Shopping")
category_repository.save(category1)

account1 = Account('Bank of Scotland', 380)
account_repository.save(account1)

company1 = Company("Tesco", 50, category1, account1)
company_repository.save(company1)

print(company1)


pdb.set_trace()
