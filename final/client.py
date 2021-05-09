from flask import Flask, request, render_template, flash

from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

import requests
import os

app = Flask(__name__)
csrf = CSRFProtect(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

SERVER_IP = "127.0.0.1"
SERVER_PORT = "5000"

class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    login = SubmitField(label='Sign in')


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/passport_page', methods=['GET', 'POST'])
def passport_page():

    form = LoginForm()
    if form.validate_on_submit():
        print("submit")
        if form.login.data == True:
            username = form.username.data
            password = form.password.data
            # response = requests.get(f"http://{SERVER_IP}:{SERVER_PORT}/api/vaccine/info",auth=(username, password))
            data = {'vacination_status': 'Fully', 'product_name':'Pfizer', 'first_does_date':'10/10/2020', 'second_dose_date':'10/10/2030', 'location':'Vandorn Pharmacy'}
            if True:
                return render_template('info.html',data=data)
            else:
                return render_template('fail_page.html')

    return render_template('login_page.html', form=form)

@app.route('/register_page', methods=['GET', 'POST'])
def register_page():

    form = LoginForm()
    if form.validate_on_submit():
        print("submit")
        if form.login.data == True:
            username = form.username.data
            password = form.password.data
            # response = requests.get(f"http://{SERVER_IP}:{SERVER_PORT}/api/vaccine/info",auth=(username, password))
            data = {'vacination_status': 'Fully', 'product_name':'Pfizer', 'first_does_date':'10/10/2020', 'second_dose_date':'10/10/2030', 'location':'Vandorn Pharmacy'}
            if True:
                return render_template('register.html',data=data)
            else:
                return render_template('fail_page.html')

    return render_template('login_page.html', form=form)

@app.route('/update_page', methods=['GET', 'POST'])
def update_page():

    form = LoginForm()
    if form.validate_on_submit():
        print("submit")
        if form.login.data == True:
            username = form.username.data
            password = form.password.data
            # response = requests.get(f"http://{SERVER_IP}:{SERVER_PORT}/api/vaccine/info",auth=(username, password))
            data = {'vacination_status': 'Fully', 'product_name':'Pfizer', 'first_does_date':'10/10/2020', 'second_dose_date':'10/10/2030', 'location':'Vandorn Pharmacy'}
            if True:
                return render_template('update.html',data=data)
            else:
                return render_template('fail_page.html')

    return render_template('login_page.html', form=form)

@app.route('/stats_page', methods=['GET', 'POST'])
def stats_page():

    form = LoginForm()
    if form.validate_on_submit():
        print("submit")
        if form.login.data == True:
            username = form.username.data
            password = form.password.data
            # response = requests.get(f"http://{SERVER_IP}:{SERVER_PORT}/api/vaccine/info",auth=(username, password))
            data = {'vacination_status': 'Fully', 'product_name':'Pfizer', 'first_does_date':'10/10/2020', 'second_dose_date':'10/10/2030', 'location':'Vandorn Pharmacy'}
            if True:
                return render_template('stats.html',data=data)
            else:
                return render_template('fail_page.html')

    return render_template('login_page.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)