from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)
    description = db.Column(db.String(500))

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Person(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.String(80)) 
    mass = db.Column(db.String(80)) 
    hair_color = db.Column(db.String(80)) 
    skin_color = db.Column(db.String(80)) 
    eye_color = db.Column(db.String(80)) 
    birth_year = db.Column(db.String(80)) 
    gender = db.Column(db.String(80)) 
    created = db.Column(db.String(80)) 
    edited = db.Column(db.String(80)) 
    name = db.Column(db.String(80)) 
    homeworld = db.Column(db.String(80)) 
    url = db.Column(db.String(80)) 

    @classmethod 
    def created(cls,**data):
        persona = cls(**data)
        if (not isinstance(persona,cls)): 
            print("Fallo en la instancia")
            return None
        db.session.add(persona)
        try:
            db.session.commit()
            return persona
        except Exception as error:
            return None

    def serialize(self):
        return{
            "id": self.id,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender" : self.gender,
            "created" : self.created,
            "edited" : self.edited,
            "name"    : self.name,
            "homeworld" : self.homeworld,
            "url"   : self.url
        }

class Planet(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    diameter = db.Column(db.String(80)) 
    rotation_period = db.Column(db.String(80)) 
    orbital_period = db.Column(db.String(80)) 
    gravity = db.Column(db.String(80)) 
    population = db.Column(db.String(80)) 
    climate = db.Column(db.String(80)) 
    terrain = db.Column(db.String(80)) 
    surface_water = db.Column(db.String(80)) 
    created = db.Column(db.String(80))
    edited = db.Column(db.String(80)) 
    name = db.Column(db.String(80)) 
    url = db.Column(db.String(80)) 

    @classmethod 
    def created(cls,**data):
        planeta = cls(**data)
        if (not isinstance(planeta,cls)): 
            print("Fallo en la instancia")
            return None
        db.session.add(planeta)
        try:
            db.session.commit()
            return planeta
        except Exception as error:
            return None

    def serialize(self):
        return{
            "id": self.id,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain" : self.terrain,
            "surface_water" : self.surface_water,
            "created" : self.created,
            "edited" : self.edited,
            "name"    : self.name,
            "homeworld" : self.homeworld,
            "url"   : self.url
        }

class Vehicle(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(80)) 
    vehicle_class = db.Column(db.String(80)) 
    manufacturer = db.Column(db.String(80)) 
    cost_in_credits = db.Column(db.String(80)) 
    length = db.Column(db.String(80)) 
    crew = db.Column(db.String(80)) 
    passengers = db.Column(db.String(80)) 
    max_atmosphering_speed = db.Column(db.String(80))
    cargo_capacity = db.Column(db.String(80))
    consumables = db.Column(db.String(80))
    films = db.Column(db.String(80))
    pilots = db.Column(db.String(80))     
    created = db.Column(db.String(80))
    edited = db.Column(db.String(80)) 
    name = db.Column(db.String(80)) 
    url = db.Column(db.String(80)) 

    @classmethod 
    def created(cls,**data):
        vehiculo = cls(**data)
        if (not isinstance(vehiculo,cls)): 
            print("Fallo en la instancia")
            return None
        db.session.add(vehiculo)
        try:
            db.session.commit()
            return vehiculo
        except Exception as error:
            return None

    def serialize(self):
        return{
            "id": self.id,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers" : self.passengers,
            "max_atmosphering_speed" : self.max_atmosphering_speed,
            "cargo_capacity" : self.cargo_capacity,
            "consumables" : self.consumables,
            "films" : self.films,
            "pilots" : self.pilots,
            "created" : self.created,
            "edited" : self.edited,
            "name"    : self.name,
            "homeworld" : self.homeworld,
            "url"   : self.url
        }

class Favorite(db.Model):
    id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    vehicle_id= db.Column(db.Integer, db.ForeignKey('vehicle.id'), primary_key=True)
    planet_id= db.Column(db.Integer, db.ForeignKey('planet.id'), primary_key=True)
    person_id= db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)

    def __repr__(self):
        return f"< user_id: {self.user_id}, Card_id: {self.card_id}>"
   
    def serialize(self):
        return {
            "user_id": self.user_id,
            "card_id": self.card_id
        }       