from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Date

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config.from_object("config")
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)

class oscar_oscarcategories (db.Model):
    id = Column(Integer, primary_key=True)
    Year = Column(Integer, nullable=False)
    Cat = Column(String(1000), nullable=False)
    Name = Column(String(1000), nullable=False)
    def __repr__(self):
        return self.name
    
class oscar_users (db.Model):
    id = Column(Integer, primary_key=True)
    Year = Column(Integer, nullable=False)
    User = Column(String(1000), nullable=False)
    Favorite = Column(String(1000), nullable=False)
    Cat = Column(String(1000), nullable=False)
    Won = Column(String(1000), nullable=False)
    def __repr__(self):
        return self.name

class oscar_winners  (db.Model):
    id = Column(Integer, primary_key=True)
    Year = Column(Integer, nullable=False)
    Cat = Column(String(1000), nullable=False)
    Name = Column(String(1000), nullable=False)
    Weight = Column(Integer, nullable=False)
    def __repr__(self):
        return self.name


admin = Admin(app, name='Oscar Admin', template_mode='bootstrap3')
admin.add_view(ModelView(oscar_oscarcategories, db.session))
admin.add_view(ModelView(oscar_users, db.session))
admin.add_view(ModelView(oscar_winners, db.session))

@app.route('/')
def hello_world():
    return 'Hello Sammy!'
