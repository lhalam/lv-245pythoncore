from wtforms import Form, StringField, IntegerField, validators

class UserForm(Form):
    username = StringField('User name', [validators.Length(min=2, max=20)])
    firstname= StringField('First name', [validators.Length(min=2, max=5)])
    lastname = StringField('Last name', [validators.Length(min=5, max=20)])
    email = StringField('Email', [validators.email()])
    password = StringField('Password', [validators.Length(min=4, max=20)])
    age = IntegerField('Age')
