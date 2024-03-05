import React from 'react';
import {Link,useParams} from "react-router-dom";

const Home = () => {
    return (
        <div>
            <h1>Welcome to View Party!</h1>
            <h2>I am a </h2>
            
            <Link to="/signup"> <button >User</button> </Link><p></p>
            <Link to="/vendersignup">   <button>Vender</button>    </Link>
        </div>
    );
};

export default Home;


