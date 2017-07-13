import os.path

from flask import Flask, request, redirect,  render_template
from flask_sqlalchemy import SQLAlchemy

from form.userForms import UserForm

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
    password = db.Column(db.String(20), nullable=True)
    

@app.route('/')
def hello_world():
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

@app.route('/user/add', methods=['GET','POST'])
def user_add():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username = form.username.data,
                    firstname = form.firstname.data,
                    lastname = form.lastname.data,
                    email = form.email.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/user')
    return render_template('user_add.html', form=form)





if __name__ == "__main__":
    db.create_all()
    app.run()
