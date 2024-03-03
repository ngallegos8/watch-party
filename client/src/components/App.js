import React, { useEffect, useState } from "react";
import { Switch, Route, Routes, createBrowserRoute, RouterProvider, BrowserRouter } from "react-router-dom";
import NavBar from './navBar'
import User from './User'

function App() {
  return(
    <BrowserRouter>
      <NavBar/>
      <main>
        <Route path="/User" element={<User/>}/>
        <Route path="/Venue" element={<User/>}/>
        <Route path="/Event" element={<User/>}/>
        
      </main>

    </BrowserRouter>


  );

}

export default App
