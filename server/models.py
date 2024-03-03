from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
#5 )pip install flask_bcrypt and import bcrypt and wrap the app in bcrypt, import hybrid property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
from datetime import datetime

metadata = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_`%(constraint_name)s`",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
    })

db = SQLAlchemy(metadata=metadata)

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True)
    #) Add the password hash attribute
    _password_hash = db.Column(db.String)
    # events_attending = db.relationship('Event', secondary='attendance', back_populates='attendees')
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

<<<<<<< HEAD
    #) Create a get method using hybrid property, and bcrypt
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    #) Create a setter method to set the password using bcrypt
    @password_hash.setter
    def password(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")
    
    #) Create an authentication method to check the password using bcrypt
    def authenticate(self, password):
        return bcrypt.check_password_hash(self.password_hash, password.encode("utf-8"))
    



class Venue(db.Model, SerializerMixin):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True)
    #) Add the password hash attribute
    _password_hash = db.Column(db.String)
    location = db.Column(db.String, unique=True, nullable=False)

    # events = db.relationship('Event', backref='venue', lazy=True)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #) Create a get method using hybrid property, and bcrypt
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    #) Create a setter method to set the password using bcrypt
    @password_hash.setter
    def password(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")
    
    #) Create an authentication method to check the password using bcrypt
    def authenticate(self, password):
        return bcrypt.check_password_hash(self.password_hash, password.encode("utf-8"))
    

class Attendance(db.Model, SerializerMixin):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), primary_key=True)

    


class Event(db.Model, SerializerMixin):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    location = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    attending_count = db.Column(db.Integer, default=0)

    # These two attributes connect the User model with the Venue model
    # STRETCH GOAL: We only care about this if the social aspect of leaving comments (think Meetup or FB events)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))

    # Here, we will add relationships to the User and Venue models

    # def __repr__(self):
    #     return '<Event %r>' % self.name

    # @validates('name')
    # def validate_name(self, key, name):
    #     assert len(name) > 2
    #     return name

    # @validates('location')
    # def validate_location(self, key, location):
    #     assert len(location) > 4
    #     return location

    # @validates('description')
    # def validate_description(self, key, description):
    #     assert len(description) > 4
    #     return description

    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'date': self.date,
    #         'location': self.location,
    #         'description': self.description,
    #         'user_id': self.user_id
    #     }

    # # Create a new event
    # new_event = Event(name="Super Bowl Watch Party", date_time=datetime(2023, 2, 12, 18, 30), location="My House", description="Come watch the Super Bowl!", user=current_user)
=======
class User():
    

    
>>>>>>> jeff
