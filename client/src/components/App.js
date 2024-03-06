import React, { useEffect, useState } from "react";
import { Switch, Route, Routes, createBrowserRoute, RouterProvider, BrowserRouter } from "react-router-dom";
import NavBar from './navBar'
import User from './User'
import Event from './Event'
import Venue from'./Venue'
import Signup from'./signup'
import VenueSignup from './venue_signup'
import Home from './Home'
import UserLogin from './userLogin'
import VenueLogin from './venueLogin'
//import UserLogin from './userLogin'




function App() {
  const [user, setUser] = useState(null);
  const [venue, setVenue] = useState(null);

  useEffect(() => {

    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => setUser(user));
      }
    });
  }, []);

  if (!user) return <UserLogin onLogin={setUser} />;

  // useEffect(() => {

  //   fetch("/check_session").then((r) => {
  //     if (r.ok) {
  //       r.json().then((venue) => setVenue(venue));
  //     }
  //   });
  // }, []);

  // if (!venue) return <VenueLogin onLogin={setVenue} />;

 
  return(
    <BrowserRouter>
      <NavBar/>
  
    
          <Switch>
          <Route exact path="/User">
            <User/>
          </Route>
          <Route exact path="/Venue">
            <Venue/>
          </Route>
          <Route exact path="/Event">
            <Event />
          </Route>
          <Route exact path="/signup/user">
            <Signup />
          </Route>
          <Route exact path="/signup/venue">
            <VenueSignup />
          </Route>
          <Route exact path="/login/user">
            <UserLogin onLogin={setUser}/>
          </Route>
          <Route exact path="/login/venue">
            <VenueLogin onLogin={setVenue}/>
          </Route>
          <Route path="/">
            <Home/>
          </Route>
          </Switch>
     
        

    </BrowserRouter>


  );

}

export default App