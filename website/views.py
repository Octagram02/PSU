#standard roots that the user can navigate
from flask import Blueprint, render_template

views = Blueprint('views',__name__) #defined a blueprint

#to find a view

@views.route('/')
def home():
    return render_template("index.html")



