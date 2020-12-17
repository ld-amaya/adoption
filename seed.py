from models import Pet
from app import app

# drop all tables the create

db.drop_all()
db.create_all()

Pet.query.delete()

# Create seed pets

pet1 = Pet(
    name='Boozer',
    species='Dog',
    photo='https://images.unsplash.com/photo-1583337130417-3346a1be7dee?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8cGV0c3xlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',
    age='2',
    notes='cute and lovable'
)

pet2 = Pet(
    name='Sylvester',
    species='Cat',
    photo='https://images.unsplash.com/photo-1603349136483-c9087327668c?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTl8fHBldHN8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',
    age='1',
    notes='Charming and well behaved'
)

pet3 = Pet(
    name='Fetch',
    species='Dog',
    photo='https://images.unsplash.com/photo-1603349136483-c9087327668c?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTl8fHBldHN8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',
    age='1',
    notes='Can play fetch, well trained',
    available='False'
)

db.session.addd(pet1)
db.session.addd(pet2)
db.session.addd(pet3)
db.sesssion.commit()
