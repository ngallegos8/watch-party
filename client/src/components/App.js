import React, { useEffect, useState } from "react";
import { Switch, Route, Routes, createBrowserRoute, RouterProvider, BrowserRouter } from "react-router-dom";
import NavBar from './navBar'
import User from './User'
import Event from './Event'
import Venue from'./Venue'

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
          <Route path="/"></Route>
          </Switch>
     
        

    </BrowserRouter>


  );

}

export default App
