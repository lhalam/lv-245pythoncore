from wtforms import Form, StringField, IntegerField, validators

class UserForm(Form):
    username = StringField('User name', [validators.Length(min=2, max=50)])
    password = StringField('Password',  [validators.Length(min=2, max=50)])
    first_name = StringField('First name', [validators.Length(min=2, max=30)])
    last_name = StringField('Last name', [validators.Length(min=5, max=30)])
    email = StringField('Email', [validators.Length(min=5, max=20)])
