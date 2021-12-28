from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import *


app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///flash-card.db'
db = SQLAlchemy(app)


app.add_url_rule('/', 'index', index)
app.add_url_rule('/login', 'login', login)
app.add_url_rule('/sign-up', 'sign-up', sign_up)





# class User(db.Model):
#     id = db.column(db.Integer, primary_key=True)



if __name__ == '__main__':
    app.run()
