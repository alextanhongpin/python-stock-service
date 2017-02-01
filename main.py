# register blueprint and start flask app
from flask import Flask
from intrinsicservice import fundamentals

app = Flask(__name__)
app.register_blueprint(fundamentals)
app.run(debug=True)