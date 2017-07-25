from wtforms import Form, StringField, IntegerField, validators

class UserForm(Form):
    firstname= StringField('First name', [validators.Length(min=2, max=10)])
    lastname = StringField('Last name', [validators.Length(min=5, max=20)])
    email = StringField('Email', [validators.Length(min=5, max=20)])
    password = StringField('Password', [validators.Length(min=5, max=20)])
