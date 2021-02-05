import pdb

from models.category import Category
from models.company import Company
from models.user import User 

import repositories.category_repostitory as category_repostitory
import repositories.company_repostitory as company_repostitory
import repositories.user_repository as user_repository

user_repository.delete_all()

user1 = User("David Taylor", 137)
user_repository.save(user1)



pdb.set_trace()
