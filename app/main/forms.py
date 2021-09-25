from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class BedRegistrationForm(FlaskForm):
        number = IntegerField('Number', validators=[DataRequired()])
        hospital = StringField('Hospital Name', validators=[DataRequired(), Length(1,64)])
        room_no = IntegerField('Room No.', validators=[DataRequired()])
        with_oxygen = BooleanField('Oxygen Available')
        is_icu = BooleanField('ICU Bed')
        with_ventilators = BooleanField('Ventilator Available')
        submit = SubmitField('Add Bed !')