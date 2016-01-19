from datetime import datetime
from flask import render_template, redirect, url_for
from . import main
from .. import db
from ..models import School, Images

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
