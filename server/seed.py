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
from models import db, User
from faker import Faker
from random import randint
faker = Faker()
with app.app_context():
    print("Deleting Customers")
    User.query.delete()

    stephen = User(username="Stephen", password="password")
    lucy = User( username="lucy", password="dogbone")
    taki = User( username="taki", password="woof")
    
    db.session.add(stephen)
    db.session.add(lucy)
    db.session.add(taki)
    db.session.commit()