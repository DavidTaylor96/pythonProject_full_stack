from flask import Flask, render_template

from controllers.category_controller import categorys_blueprint
from controllers.company_controller import companys_blueprint
from controllers.user_controller import users_blueprint

app = Flask(__name__)

app.register_blueprint(users_blueprint)
app.register_blueprint(companys_blueprint)
app.register_blueprint(categorys_blueprint)


if __name__ == '__main__':
  app.run(debug=True)