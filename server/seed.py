#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db




# # Create a new event
    # new_event = Event(name="Super Bowl Watch Party", date_time=datetime(2023, 2, 12, 18, 30), location="My House", description="Come watch the Super Bowl!", user=current_user)

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
