from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForms

app = Flask(__name__)
# app.debug = True

app.config['SECRET_KEY'] = 'iamlou'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

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


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Handles the add pet form"""

    form = PetForms()
    if form.validate_on_submit():
        # pet = Pet(name=form.name.data,
        #           species=form.species.data,
        #           photo=form.photo.data,
        #           age=form.age.data,
        #           notes=form.notes.data)
        data = {key: value for key, value in form.data.items() if key !=
                'csrf_token'}
        pet = Pet(**data)
        db.session.add(pet)
        db.session.commit()
        flash(f"New pet {form.name.data} added")
        return redirect("/")
    else:
        return render_template("/add_pet.html", form=form)
