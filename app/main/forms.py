#-*-coding: utf-8-*-

from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, IntegerField, RadioField,\
                SelectField, FileField, SubmitField
from wtforms.validators import Required
from ..models import RiyadhSchools, RiyadhImages

class SeachForm(Form):
    city = SelectField(u'المدينة', choices=[('riyadh', 'الرياض'), ('jeddah',\
                'جدة'), ('dammam', 'الدمام')])
    levels
