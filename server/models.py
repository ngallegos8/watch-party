from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
#5 )pip install flask_bcrypt and import bcrypt and wrap the app in bcrypt, import hybrid property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import Bcrypt
import requests

#) NEED TO ADD FOR ADDRESS VALIDATION
# GOOGLE_MAPS_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'

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
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

<<<<<<< HEAD
    events_attending = db.relationship('Event', secondary='attendance', back_populates='attendees')
    serialize_rules = ('-events_attending.attendees', )

=======
>>>>>>> jeff
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
    
    @validates('username')
    def validate_username(self, key, value):
        if(1 < len(value)):
            return value
        else:
            raise ValueError("Username must be greater than 1 character")
    



class Venue(db.Model, SerializerMixin):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True)
    #) Add the password hash attribute
    _password_hash = db.Column(db.String)
    location = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    events = db.relationship('Event', back_populates='venues')
    serialize_rules = ('-events.venues', )

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
    
    @validates('username')
    def validate_username(self, key, value):
        if(1 < len(value)):
            return value
        else:
            raise ValueError("Username must be greater than 1 character")
    
    @staticmethod
    def is_valid_address(address):
        google_maps_api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
        response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json',
            params={
                'address': address,
                'key': google_maps_api_key
            }
        )
        if response.status_code == 200:
            result = response.json()
            if result['status'] == 'OK':
                return True
        return False

    @validates('location')
    def validate_location(self, key, value):
        if self.is_valid_address(value):
            return value
        else:
            raise ValueError("Invalid address")
        
    



class Attendance(db.Model, SerializerMixin):
    __tablename__ = 'attendees'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), primary_key=True)

    attendees = db.relationship('User', secondary='attendance', back_populates='event')
    events_attending = db.relationship('Event', secondary='attendance', back_populates='attendees')

    serialize_rules = ('-attendees.event', 'events_attending.attendees')




class Event(db.Model, SerializerMixin):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.String)
    attending_count = db.Column(db.Integer, default=0)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    # STRETCH GOAL: We only care about this if the social aspect of leaving comments (think Meetup or FB events)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    venues = db.relationship('Venue', back_populates='events')
    attendees = db.relationship('User', secondary='attendance', back_populates='events_attending')
    serialize_rules = ('-venues.events', 'attendees.events_attending')


    @validates('name')
    def validate_name(self, key, value):
        if(1 <= len(value) <= 20):
            return value
        else:
            raise ValueError("Event name must be less than 20 Characters")

    @validates('description')
    def validate_description(self, key, value):
        if(1 <= len(value) <= 100):
            return value
        else:
            raise ValueError("Event name must be less than 100 Characters")


    def __repr__(self):
        return f'<Event: {self.name}: {self.date_time}, {self.venue}>'

    # # Create a new event
    # new_event = Event(name="Super Bowl Watch Party", date_time=datetime(2023, 2, 12, 18, 30), location="My House", description="Come watch the Super Bowl!", user=current_user)
