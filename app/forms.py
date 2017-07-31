from flask_wtf import Form
from wtforms import StringField, BooleanField, validators

class LoginForm(Form):
    identifier = StringField("identifier", [validators.Length(min=64, max=64)])
    remember_me = BooleanField("remember_me", default=False)
