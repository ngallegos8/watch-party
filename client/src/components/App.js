import React, { useEffect, useState } from "react";
import { Switch, Route, createBrowserRoute, RouterProvider, BrowserRouter } from "react-router-dom";
import NavBar from './navBar'

function App() {
  return(
    <BrowserRouter>
      <NavBar/>

    </BrowserRouter>


  );

}

export default App
