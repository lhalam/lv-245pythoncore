import os.path

from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

from form.userForms import UserForm
from form.profileForm import ProfileForm


app = Flask(__name__)#app = Flask(__name__, static_url_path='')<--------------------------------------------------------------------------------------

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'myApp.sqlite')

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=True)

    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.query.get(user_id)
            return user
        except Exception:
            return None

    def __repr__(self):
        return "{} {}".format(self.id, self.firstname)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(20), nullable=True)
    zip_code = db.Column(db.Integer, nullable=True)

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


class Contact(db.Model):
    owner_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)

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
        user = User(firstname=form.firstname.data,
                    lastname=form.lastname.data,
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
            form.firstname.data = user.firstname
            form.lastname.data = user.lastname
            form.age.data = user.age
        if request.method == 'POST' and form.validate():
            user.firstname = form.firstname.data
            user.lastname = form.lastname.data
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
                          city=form.city.data,
                          zip_code=form.zip_code.data)
        db.session.add(profile)
        db.session.commit()
        _url = '/user/' + str(user_id)
        return redirect(_url)
    # print form.errors
    return render_template('profile_add.html', form=form)

@app.route('/profile/<profile_id>/delete', methods=['GET'])
def profile_del(profile_id):
    profile = Profile.get_by_id(profile_id)
    user_id = profile.user_id
    if profile:
        db.session.delete(profile)
        db.session.commit()
        return redirect('/user/{}'.format(user_id))#<----------------------------------------------------------------------------------
    return render_template('error.html', msg_eror="not id {}".format(user_id))

@app.route('/user/<user_id>/contact', methods=['GET'])
def contact(user_id):
    users = User.query.all()
    users = [user for user in users if not user.id == int(user_id)]
        

    if request.method == "GET":
        return render_template('contact_list.html', users=users)


if __name__ == "__main__":
    db.create_all()
    app.run()