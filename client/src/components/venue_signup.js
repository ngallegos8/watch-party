import {useEffect, useState} from "react";

function VenueSignup() {
    const [user, setUser] = useState(null)
    const [name, setName] = useState("")
    const [password, setPassword] = useState("")
    const [location, setLocation] = useState("")
    const [venueName, setVenueName] = useState("")

    useEffect(() => {
        fetch("/check_session").then((r) => {
            if (r.ok) {
                r.json()
                .then((user) => setUser(user))
            }
        })
    }, [])


    function handleSignup(e){
        e.preventDefault()
        fetch("/signup/venue", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                name: name,
                password: password,
                location: location,
                venue_name: venueName
            })
        })
        .then(r => r.json())
        .then(data => setUser(data))
    }

    function handleLogout(){
        fetch("/logout", {
            method: "DELETE"
        })
        .then(setUser(null))
    }

    if(user){
        return (
            <>
            <h1>Welcome, {user.username}</h1>
            <button onClick={handleLogout}>Logout</button>
            </>
        )
    }
    else {
        return(
            <>
                <h1>New Venue</h1>
                <form onSubmit={handleSignup}>
                        <label>Enter Username</label>
                        <input type="text" value={name} onChange={(e) => setName(e.target.value)}></input><p></p>

                        <label>Enter Password</label>
                        <input type="text" value={password} onChange={(e) => setPassword(e.target.value)}></input><p></p>

                        <label>Enter Location</label>
                        <input type="text" value={location} onChange={(e) => setLocation(e.target.value)}></input><p></p>

                        <label>Enter Venue Name</label>
                        <input type="text" value={venueName} onChange={(e) => setVenueName(e.target.value)}></input><p></p>

                        <button type="submit">Submit</button>
                </form>
            </>
        )
    }
}

export default VenueSignup;