import {Link,useParams} from "react-router-dom";

function NavBar(){
    return(
     <div>
        <nav class="navbar">
            <Link to="/">  Home    </Link>
            
            <Link to="/User">  User    </Link>
            
            <Link to="/Event">  Event    </Link>
            
            <Link to="/Venue">  Venue    </Link>
            
            
        </nav>
     </div>


    )


}
export default NavBar