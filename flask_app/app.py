import os.path

from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

from form.userForms import UserForm
from form.profileForm import ProfileForm


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'myApp.sqlite')

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)

    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.query.get(user_id)
            return user
        except Exception:
            return None


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    bday = db.Column(db.Integer, nullable=True)
    sex = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    zip_code = db.Column(db.Integer, nullable=True)
    phone = db.Column(db.Integer, nullable=True)

    @staticmethod
    def get_by_id(user_id):
        try:
            profile = Profile.query.get(user_id)
            return profile
        except Exception:
            return None

    @staticmethod
    def get_by_user_id(user_id):
        try:
            profile = Profile.query.filter_by(user_id=user_id).first()
            return profile
        except Exception:
            return None

class Contact(db.Model):#<-----------------------------------------------------------------------------------
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    @staticmethod
    def create(owner_id, user_id):
        contact = Contact(owner_id=owner_id,
                          user_id=user_id)
        db.session.add(contact)
        db.session.commit()

    @staticmethod
    def get(owner_id):
        contacts = Contact.query.filter_by(owner_id=owner_id)
        return contacts


@app.route('/')
def index():
    return render_template('main_page.html')


@app.route('/user', methods=['GET'])
def user_get():
    users = User.query.all()
    return render_template('user.html', users=users)

@app.route('/user/add', methods=['GET','POST'])
def user_add():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data,
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    password=form.password.data,
                    age=form.age.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/user')
    return render_template('user_add.html', form=form)

@app.route('/user/<user_id>/delete', methods=['GET'])
def user_del(user_id):
    user = User.get_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect('/user')
    return render_template('error.html', msg_eror="not id {}".format(user_id))

@app.route('/user/<user_id>/info', methods=['GET'])
def user_info_one(user_id):
    user = User.get_by_id(user_id)
    profile = Profile.get_by_user_id(user_id)
    return render_template('user_info_one.html',user=user, profile=profile)

@app.route('/user/<user_id>', methods=['GET','POST'])
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
            form.password.data = user.password
            form.age.data = user.age
        if request.method == 'POST' and form.validate():
            user.username=form.username.data
            user.firstname = form.firstname.data
            user.lastname = form.lastname.data
            user.email = form.email.data
            user.password = form.password.data
            user.age = form.age.data
            db.session.add(user)
            db.session.commit()
        return render_template('user_info.html', user=user, profile=profile, form=form)
    return render_template('error.html', msg_eror="not id {}".format(user_id))

@app.route('/user/<user_id>/profile', methods=['GET','POST'])
def profile_post_get(user_id):
    form = ProfileForm(request.form)
    if request.method == 'POST' and form.validate():
        profile = Profile(user_id=user_id,
                          bday=form.bday.data,
                          sex=form.sex.data,
                          city=form.city.data,
                          zip_code=form.zip_code.data,
                          phone=form.phone.data)
        db.session.add(profile)
        db.session.commit()
        _url = '/user/' + str(user_id)
        return redirect(_url)
    return render_template('profile_add.html', form=form)

@app.route('/profile/<profile_id>/delete', methods=['GET'])
def profile_del(profile_id):
    profile = Profile.get_by_id(profile_id)
    user_id = profile.user_id
    if profile:
        db.session.delete(profile)
        db.session.commit()
        return redirect('/user/{}'.format(user_id))
    return render_template('error.html', msg_eror="not id {}".format(user_id))

@app.route('/user/<owner_id>/contact', methods=['GET'])
def contact(owner_id):
    users = User.query.all()
    users = [user for user in users if not user.id == int(owner_id)]
    return render_template('contact_list.html', users=users, owner_id=owner_id)



@app.route('/user/<user_id>/contact/add/<id>', methods=['GET'])
def add_contact(user_id, id):
    contact = Contact(owner_id = user_id, user_id = id)
    db.session.add(contact)
    db.session.commit()
    return redirect('/user/{}/contact'.format(user_id))






if __name__ == "__main__":
    db.create_all()
    app.run()