import {Link,useParams} from "react-router-dom";

function NavBar(){
    return(
     <div>
        <nav class="navbar">
            <Link to="/">  Home    </Link>
            
            <Link to="/">  User    </Link>
            
            <Link to="/">  Event    </Link>
            
            <Link to="/">  Venue    </Link>
            
            
        </nav>
     </div>


    )


}
export default NavBar