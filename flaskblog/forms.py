from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import TextAreaField, SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flaskblog.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20) ])
    email = StringField('Email', validators=[ DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username is taken . Please choose different one!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email is taken . Please choose different one!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login ')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Upload profile pic', validators=[FileAllowed( ['jpg', 'png'] )])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError('Username is taken . Please choose different one!')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError(
                    'Email is taken . Please choose different one!')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request password reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user is None:
            raise ValidationError(
                'There is not account with email please do register')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset password')
