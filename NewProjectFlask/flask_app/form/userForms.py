from wtforms import Form, StringField, IntegerField, validators

class UserForm(Form):
    first_name = StringField('First name', [validators.Length(min=2, max=30)])
    last_name = StringField('Last name', [validators.Length(min=2, max=30)])    
    password = StringField('Password', [validators.Length(min=2, max=50)])    
    email = StringField('Email Address', [validators.Length(min=2, max=20)])
