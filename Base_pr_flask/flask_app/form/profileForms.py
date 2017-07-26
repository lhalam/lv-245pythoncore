from wtforms import Form, StringField, IntegerField, validators

class ProfileForm(Form):
    bday = StringField('Birthday', [validators.Length(min=2, max=30)])
    sex = StringField('Sex', [validators.Length(min=2, max=30)])
    city = StringField('City', [validators.Length(min=2, max=30)])
    zip_code = IntegerField('Zip code')
    phone = IntegerField('Phone')