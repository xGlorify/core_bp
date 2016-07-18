from flask import Flask, g, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
from flask.ext.bcrypt import Bcrypt
from assets.forms import SearchAssetTag

app = Flask(__name__ )
app.config.from_object('config')
login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from users.views import users_blueprint
from assets.views import assets_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(assets_blueprint,  url_prefix = '/assets')

#db.drop_all()
#db.create_all()
#db.session.commit()
#db.session.rollback()

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

@app.before_request #Define headersearchform globally as it runs on every page with header.
def before_request():
    g.headersearchform = SearchAssetTag()
    g.current_user = current_user
    
login_manager.login_view = "users.login"

from users.models import User

@app.route('/')
def global_redirect():
    return redirect(url_for('assets.viewassets'))

if __name__ == "__main__":
  app.run(host="192.168.168.66", debug = True, threaded = True)
