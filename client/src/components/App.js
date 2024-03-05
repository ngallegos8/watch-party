import React, { useEffect, useState } from "react";
import { Switch, Route, Routes, createBrowserRoute, RouterProvider, BrowserRouter } from "react-router-dom";
import NavBar from './navBar'
import User from './User'
import Event from './Event'
import Venue from'./Venue'
import Signup from'./signup'
import VenueSignup from './venue_signup'

function App() {
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
          <Route path="/">
            <Home/>
          </Route>
          </Switch>
     
        

    </BrowserRouter>


  );

}

export default App
//