# #!/usr/bin/env python3

# # Standard library imports#
# from random import randint, choice as rc

# # Remote library imports
# from faker import Faker

# # Local imports
# from app import app
# from models import db, User, Venue, Event, Attendance



# if __name__ == '__main__':p
#     fake = Faker()
#     with app.app_context():
#         print("Deleting Customers")
#         User.query.delete()

#     stephen = User(username="Stephen", password="password")
#     db.session.add(stephen)
#     db.session.commit()

from app import app 
from models import db, User, Event
from faker import Faker
from random import randint
from datetime import datetime
import datetime

faker = Faker()
with app.app_context():
    print("Deleting Customers")
    User.query.delete()

    stephen = User(username="Stephen", password="password")
    lucy = User( username="lucy", password="dogbone")
    taki = User( username="taki", password="woof")

    date_time_str = "2024, 5, 1, 23, 0, 0"
    date_time_obj = datetime.datetime(*map(int, date_time_str.split(", ")))

    boxingMatch = Event(name ="boxing match", date_time=date_time_obj, description="a boxing match", attending_count="5")
    
    db.session.add(stephen)
    db.session.add(lucy)
    db.session.add(taki)

    db.session.add(boxingMatch)
    db.session.commit()



    # events
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String, nullable=False)
    # date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # description = db.Column(db.String)
    # attending_count = db.Column(db.Integer, default=0)
    # venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))