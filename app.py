from flask import Flask, request, render_template, redirect, session, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForms, EditPetForm

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


# GET Requests
@app.route("/")
def home():
    """Manages home page"""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)


@app.route("/species/<specie>")
def view_specie(specie):
    """Handles Specific Specie"""
    pets = Pet.query.filter_by(species=specie).all()
    return render_template("/species.html", pets=pets)


@app.route("/available")
def view_available_pets():
    """Displays Available Pets Only"""
    pets = Pet.query.filter_by(available=True).all()
    return render_template("index.html", pets=pets)


@app.route("/not_available")
def view_not_available_pets():
    """Displays Not Available Pets Only"""
    pets = Pet.query.filter_by(available=False).all()
    return render_template("index.html", pets=pets)


@app.route("/<int:id>")
def view_pet(id):
    """Display Pet Information"""
    pet = Pet.query.get_or_404(id)
    return render_template("/pet.html", pet=pet)


######### CREATE REQUESTS ###########################
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


######## UPDATE REQUESTS #####################################

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_pet(id):
    """Display Pet Information"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo = form.photo.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Pet {pet.name} Updated")
        return redirect(f"/{pet.id}")
    else:
        return render_template("/pet_edit.html", pet=pet, form=form)


######### Handles API GET Requests ###################################

@app.route("/api/pets/<int:id>")
def pet_api_id_based(id):
    """Return basic information about a pet id"""
    pet = Pet.query.get_or_404(id)
    info = {"name": pet.name,
            "species": pet.species,
            "age": pet.age}
    return jsonify(info)


@app.route("/api/pets")
def pet_api_all():
    """Return basic information about the pet"""
    pets = Pet.query.all()
    data = []
    for pet in pets:
        info = {'name': pet.name,
                'species': pet.species,
                'age': pet.age}
        data.append(info)
    return jsonify(data)
