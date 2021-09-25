from wtforms.fields.core import IntegerField
from app.models import Hospital
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class LoginForm(FlaskForm):
        email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
        password = PasswordField('Password', validators=[DataRequired()])
        remember_me = BooleanField('Keep me logged in')
        submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
        name = StringField('Name', validators=[DataRequired(), Length(1,64)])
        email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
        pincode = IntegerField('PinCode', validators=[DataRequired()])
        password = PasswordField('Enter Password', 
                                        validators=[DataRequired(), 
                                                EqualTo('repassword', message="Passwords must match")])
        repassword = PasswordField('Re-enter Password',
                                        validators=[DataRequired()])
        submit = SubmitField('Register')

        def verify_email(self, email):
                if Hospital.query.filter_by(email=email.data).first():
                        raise ValidationError("User already registered")