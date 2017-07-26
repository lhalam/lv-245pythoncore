from wtforms import Form, StringField, IntegerField, validators, DateField, SelectField

class ProfileForm(Form):
    bday = DateField('Bday', format='%m/%d/%Y')
    sex = SelectField('Sex', choices=[('M', 'Male'), ('F', 'Female')])
    city = StringField('City', [validators.Length(min=2, max=20)])
    zip_code = IntegerField('ZIP code')
    phone = IntegerField('Phone')