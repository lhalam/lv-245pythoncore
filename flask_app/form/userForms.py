from wtforms import Form, StringField, IntegerField, validators

class UserForm(Form):
    firstname = StringField('First name', [validators.Length(min=2, max=5)])
    lastname = StringField('Last name', [validators.Length(min=2, max=20)])
    age = IntegerField('Age')
