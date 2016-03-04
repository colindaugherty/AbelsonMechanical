from flask import Flask
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config.from_envvar('ABELSON_SETTINGS', silent=True)

import abelson.views
