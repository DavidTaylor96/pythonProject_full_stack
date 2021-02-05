from flask import Flask, render_template

from controllers.category_controller import category_controller
from controllers.company_controller import company_controller
from controllers.user_controller import user_controller

app = Flask(__name__)

app.register_blueprint(users_blueprint)
app.register_blueprint(companys_blueprint)
app.register_blueprint(categorys_blueprint)


@app.route('/')
def home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)