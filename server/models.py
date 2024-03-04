from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class User():
    pass

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