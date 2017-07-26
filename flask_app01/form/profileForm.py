from wtforms import Form, StringField, IntegerField, validators

class ProfileForm(Form):
    bday = StringField('Birthday', [validators.Length(min=2, max=30)])
    sex = StringField('Sex', [validators.Length(min=2, max=30)])
    city = StringField('City', [validators.Length(min=2, max=50)])
    zip_code = IntegerField('ZIP code')
    phone = IntegerField('Phone', [validators.Length(min=5, max=15)])