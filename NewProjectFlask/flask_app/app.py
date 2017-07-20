import os.path

from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

from form.userForms import UserForm

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'myApp.sqlite')

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.query.get(user_id)
            return Profile
        except Exception, e:
            return None

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    bday = db.Column(db.String(30), nullable=True)
    sex = db.Column(db.String(5), nullable=True)
    city = db.Column(db.String(30), nullable=True)
    zip_code = db.Column(db.Integer, nullable=True)
    phone = db.Column(db.Integer, nullable=True)

    @staticmethod
    def get_by_id(user_id):
        try:
            profile = Profile.query.get(user_id)
            return profile
        except Exception, e:
            return None
            
    @staticmethod
    def get_by_user_id(user_id):
        try:
            profile = Profile.query.filter_by(user_id=user_id).first()
            return profile
        except Exception, e:
            return None

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return """
            <a href='http://localhost:5000/user'>user</a><br>
            <a href='http://localhost:5000/user/add'>add user</a><br>
            """

@app.route('/test')
def hello_world_test():
    return 'test Hello, World!'


@app.route('/user', methods=['GET'])
def user_get():
    users = User.query.all()
    return render_template('user.html', us=users)

# @app.route('/user/<user_id>', methods=['GET'])
# def user_get(user_id):
#     users = User.get_by_id(user_id)
#     if user:

#     return render_template('user.html', us=users)

@app.route('/user/<user_id>/profile', methods=['GET','POST'])
def profile_post_get(user_id):
    form = 

@app.route('/user/add', methods=['GET','POST'])
def user_add():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username = form.username.data,
                    password = form.password.data,
                    first_name = form.first_name.data,
                    last_name = form.last_name.data,
                    email = form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/user')
    return render_template('user_add.html', form=form)





if __name__ == "__main__":
    db.create_all()
    app.run()
