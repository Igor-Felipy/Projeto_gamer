from flask import Flask 

app = Flask(__name__)
from app.models import main as main_blueprint 
app.register_blueprint(main_blueprint)