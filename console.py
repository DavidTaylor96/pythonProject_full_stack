import pdb

from models.category import Category
from models.company import Company
from models.user import User 

import repositories.category_repository as category_repository
import repositories.company_repository as company_repository
import repositories.user_repository as user_repository

user_repository.delete_all()
category_repository.delete_all()
company_repository.delete_all()

user1 = User("David Taylor", 137)
user_repository.save(user1)

category1 = Category("Entertainment")
category_repository.save(category1)

company1 = Company("Tesco", category1, 50)
company_repository.save(company1)


pdb.set_trace()
