import os.path
import hashlib

from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from form.userForms import UserForm
from form.profileForm import ProfileForm

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=True)

    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.query.get(user_id)
            return user
        except(Exception):
            return None

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(20), nullable=True)
    zip_code = db.Column(db.Integer, nullable=True)
    phone = db.Column(db.Integer, nullable=True)

    @staticmethod
    def get_by_id(user_id):
        try:
            profile = Profile.query.get(user_id)
            return profile
        except Exception as e:
            return None

    @staticmethod
    def get_by_user_id(user_id):
        try:
            profile = Profile.query.filter_by(user_id=user_id).first()
            return profile
        except Exception as e:
            return None

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/user', methods=['GET'])
def user_get():
    users = User.query.all()
    pro = []
    for user in users:
        user.profile = Profile.get_by_user_id(user.id)
        pro.append(user)
    return render_template('user.html', us=pro)


@app.route('/user/add', methods=['GET', 'POST'])
def user_add():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data,
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    password=hashlib.md5(form.password.data.encode()).hexdigest())
        db.session.add(user)
        db.session.commit()
        return redirect('/user')
    # print("tesr")
    return render_template('user_add.html', form=form)

@app.route('/user/<user_id>/delete', methods=['GET'])
def user_del(user_id):
    user = User.get_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect('/user')
    return render_template('error.html', msg_eror="not id {}".format(user_id))


@app.route('/user/<user_id>/edit', methods=['GET','POST'])
def user_update(user_id):
    user = User.get_by_id(user_id)
    if user:
        profile = Profile.get_by_user_id(user.id)
        form = UserForm(request.form)
        if request.method == 'GET':
            form.username.data = user.username
            form.firstname.data = user.firstname
            form.lastname.data = user.lastname
            form.email.data = user.email
        if request.method == 'POST' and form.validate():
            user.username = form.username.data
            user.firstname = form.firstname.data
            user.lastname = form.lastname.data
            user.email = form.email.data
            db.session.add(user)
            db.session.commit()
        return render_template('user_info.html', user=user, profile=profile, form=form)
    return render_template('error.html', msg_eror="not id {}".format(user_id))


@app.route('/user/<user_id>/profile', methods=['GET','POST'])
def profile_post_get(user_id):
    form = ProfileForm(request.form)
    print  form.validate()
    if request.method == 'POST' and form.validate():
        profile = Profile(user_id=user_id,
                          city=form.city.data,
                          zip_code=form.zip_code.data,
                          phone=form.phone.data)
        db.session.add(profile)
        db.session.commit()
        _url = '/user/' + str(user_id) + "/edit"
        return redirect(_url)
    print form.errors
    return render_template('profile_add.html', form=form)

if __name__ == "__main__":
    db.create_all()
    app.run()
