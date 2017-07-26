from wtforms import Form, StringField, IntegerField, validators

class ProfileForm(Form):
    birthday = StringField('Birthday', [validators.Length(min=2, max=50)])
    sex = StringField('Sex', [validators.Length(min=2, max=50)])
    city = StringField('City', [validators.Length(min=2, max=50)])
    zip_code = IntegerField('ZIP code')
    phone = IntegerField('Numbe Phone')
