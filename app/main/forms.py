#-*-coding: utf-8-*-

from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, IntegerField, RadioField,\
                SelectField, FileField, SubmitField, BooleanField
from wtforms.validators import Required
from ..models import RiyadhSchools, RiyadhImages

class SeachForm(Form):
    city = SelectField('city', choices=[('riyadh', u'الرياض'), ('jeddah',\
                u'جدة'), ('dammam', u'الدمام')])

    rawdha = BooleanField(u'روضة')
    tamhedy = BooleanField(u'تمهيدي')
    elementary = BooleanField(u'ابتدائي')
    intermediate = BooleanField(u'متوسط')
    high_school = BooleanField(u'ثانوي')

    gender = RadioField('gender', choices=[('boys', u'بنين'),('girls', u'بنات'), \
        ('both', u'الكل')])

    submit = SubmitField('submit')

class AddSchoolForm(Form):
    schoolName = StringField(u'اسم المدرسة', validators=[Required(), Length(1, 64)])
    schoolBio = TextAreaField(u'عن المدرسة', validators=[Required()])
    schoolCity = SelectField('city', choices=[('riyadh', u'الرياض'), ('jeddah',\
                u'جدة'), ('dammam', u'الدمام')])
    schoolAddress = StringField(u'العنوان', validators=[Required(), Length(1, 100)])
    schoolPhone = IntegerField(u'الهاتف', val)

class ContactForm(Form):
