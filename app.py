from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
admin = Admin(app, name='oscar', template_mode='cerlean')

admin.add_view(ModelView(User, db.session))


@app.route('/')
def hello_world():
    return 'Hello Sammy!'
