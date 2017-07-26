from wtforms import Form, StringField, IntegerField, validators

class ProfileForm(Form):
    city = StringField('City', [validators.Length(min=2, max=50)])
    zip_code = IntegerField('ZIP code')
    phone = IntegerField('Phone')
