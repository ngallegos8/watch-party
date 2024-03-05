#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, session
from flask_restful import Resource

# Local imports
from config import app, api
#) ✅ python -c 'import os; print(os.urandom(16))'
#) Used to hash the session data
app.secret_key = b'*\x10\x1eI~\n=\xe6\x92\xb4N\xe1\x94\x8b\xea\xb8'


# Add your model imports
from models import db, User, Venue, Event, Attendance


# Views go here!
@app.route('/')
def index():
    return '<h1>Project Server</h1>'

#) Use @app.before_request, to run a function that checks if the session has the correct user, before every request
    #) Test this route out in client
@app.before_request
def check_session():
    if session.get("user_id") is None:
        session["user_id"] = None
    if session.get("venue_id") is None:
        session["venue_id"] = None
    else:
        print("User is logged in")
        print(session["user_id"])
        print(session["venue_id"])


class SignUpUser(Resource):
    def post(self):
        form_json = request.get_json()
        new_user = User(
            username = form_json["name"],
            password = form_json["password"]
        )
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id
        print(session["user_id"])
        return new_user.to_dict(), 201
api.add_resource(SignUpUser, '/signup/user')

class SignUpVenue(Resource):
    def post(self):
        form_json = request.get_json()
        new_venue = Venue(
            username = form_json["name"],
            password = form_json["password"],
            location = form_json["location"],
            venue_name = form_json["venue_name"]
        )
        db.session.add(new_venue)
        db.session.commit()
        session["user_id"] = new_venue.id
        print(session["venue_id"])
        return new_venue.to_dict(), 201
api.add_resource(SignUpVenue, '/signup/venue')

#) Create a logout route now! set session to None, and test this route out in client
class LogOut(Resource):
    def delete(self):
        if session.get("user_id"):
            session["user_id"] = None
        if session.get("venue_id"):
            session["venue_id"] = None
        return {}, 204
    
api.add_resource(LogOut, "/logout")


#) Create a route to sign in and authenticate the user
    #)Test this route out in client
        
#) Create a Login route that will save a user to the session
    #) Create a login class that inherits from Resource
    #) Use api.add_resource to add the '/login' path
    #) Build out the post method
        #) convert the request from json and select the user name sent form the client. 
        #) Use the name to query the user with a .filter
        #) If found set the user_id to the session hash
        #) convert the user to_dict and send a response back to the client
    # Test this route out in client
class Login(Resource):
    def post(self):
        form_json = request.get_json()
        username = form_json["username"]
        password = form_json["password"]
        user = User.query.filter(User.username == username).first()
        venue = Venue.query.filter(Venue.username == username).first()
        if user and user.authenticate(password):
            session["user_id"] = user.id
            return user.to_dict(), 200
        elif venue and venue.authenticate(password):
            session["venue_id"] = venue.id
            return venue.to_dict(), 200
        else:
            return "Invalid Credentials", 401
        
api.add_resource(Login, "/signin")

class CheckSession(Resource):
    def get(self):
        user_id = session["user_id"]

        if user_id:
            user = User.query.filter(User.id == user_id).first()
            return user.to_dict(), 200
        return {}, 401
    
api.add_resource(CheckSession, "/check_session")



class AllEvents(Resource): # This class will be used to GET (read) all events & POST (create) a new event

    def get(self): # GET method to retrieve all events
        events = Event.order_by('created_at').all() # we could also make this Event.query.all()
        return [event.to_dict() for event in events], 200 
    
    def post(self): # POST method to create a new event
        data = request.get_json()
        new_event = Event(
            name = data["name"],
            date = data["date"], # should we use date_time here like we did in Models.py? 
            description = data["description"]
        )
        db.session.add(new_event)
        db.session.commit()

        response = make_response(
            new_event.to_dict(), 201
        )
        return response 

api.add_resource(AllEvents, "/events") # This is the route for the AllEvents class

 
class EventByID(Resource): # This class will be used to GET (read) a single event, PATCH (update) a single event, & DELETE a single event
    def get(self, id):
        event_dict = Event.query.filter_by(id=id).first().to_dict()

        response = make_response(
            event_dict, 200
        )
        return response

    def patch(self, id):
        event = Event.query.filter_by(id=id).first()
        data = request.get_json()
        # event.name = data["name"]
        # event.date = data["date"]
        # event.description = data["description"]
        for attr in data:
            setattr(event, attr, data[attr])
        db.session.add(event)
        db.session.commit()
        return make_response(event.to_dict(), 200)
    
    def delete(self, id):
        event = Event.query.filter_by(id=id).first()
        db.session.delete(event)
        db.session.commit()
        return make_response( {'deleted': True}, 204 )

api.add_resource(EventByID, "/events/<int:id>") 


class AllVenues(Resource): # This class will be used to GET (read) all venues & POST (create) a new venue

    def get(self): # GET method to retrieve all venues
        venues = Venue.query.all()
        return [venue.to_dict() for venue in venues], 200 
    
    def post(self): # POST method to create a new venue
        data = request.get_json()
        new_venue = Venue(
            name = data["name"],
            location = data["location"]
        )
        db.session.add(new_venue)
        db.session.commit()

        response = make_response(
            new_venue.to_dict(), 201
        )
        return response
    
api.add_resource(AllVenues, "/venues") # This is the route for the AllVenues class which gets all venes & lets a user create a new venue 



if __name__ == '__main__':
    app.run(port=5555, debug=True)

