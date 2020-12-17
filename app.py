from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iamlou'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///pet_adoption"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route("/")
def home():
    """Manages home page"""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)
