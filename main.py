# register blueprint and start flask app
import os
from flask import Flask
from intrinsicservice import fundamentals
from costservice import costs


port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
app.register_blueprint(fundamentals)
app.register_blueprint(costs)
# app.run(debug=True)
app.run(host='0.0.0.0', port=port)