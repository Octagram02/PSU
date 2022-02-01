from flask import Flask

def create_app():
    app = Flask(__name__) # it represents the file that is ran
    app.config['SECRET_KEY'] = 'wewewewewewe'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")  #access the views
    app.register_blueprint(auth, url_prefix="/")   #access the auth
    return app