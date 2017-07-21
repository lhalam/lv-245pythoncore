from wtforms import Form, StringField, IntegerField, validators

class UserForm(Form):
    first_name = StringField('First name', [validators.Length(min=2, max=5)])
    last_name = StringField('Last name', [validators.Length(min=5, max=20)])
    age = IntegerField('Age')