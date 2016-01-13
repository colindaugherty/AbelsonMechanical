from flask import Flask

app = Flask(__name__)
app.config.from_envvar('ABELSON_SETTINGS', silent=True)

import abelson.views
