from flask import Blueprint, render_template

auth = Blueprint('auth',__name__) #defined a blueprint

@auth.route('/appointment', methods=['GET','POST'])
def appoint():
    return  render_template("Appointment.html")

@auth.route('/1st-dose', methods=['GET','POST'])
def appoint1():
    return  render_template("Appointment1.html")

@auth.route('/booster', methods=['GET','POST'])
def booster():
    return  render_template("Booster.html")

@auth.route('/how-to-get-vaccinated')
def info():
    return  render_template("about.html")


@auth.route('/htga', methods=['GET','POST'])
def htga():
    return  render_template("htga.html")

@auth.route('/htga1', methods=['GET','POST'])
def htga1():
    return  render_template("htga1st.html")

@auth.route('/htga3', methods=['GET','POST'])
def htga3():
    return  render_template("htgaboost.html")

@auth.route('/samp', methods=['GET','POST'])
def sample():
    return  render_template("sample.html")

