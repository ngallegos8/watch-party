import React, { useState } from "react";

function EventCard({ event, removeEvent, updateEvent }) {
  
  const [attend, setAttend] = useState("")
  const [attendingCount, setAttendingCount] = useState("")
  const [venue, setVenue] = useState("")
  const [name, setName] = useState("")
  const [dateTime, setDateTime] = useState("")
  const [description, setDescription] = useState("")


  function handleDelete() {
    fetch(`http://127.0.0.1:5555/events/${event.id}`, {
      method: "DELETE"
    })
    removeEvent(event.id)
  }

  function handleUpdateSubmit(e) {
    e.preventDefault()
    fetch(`http://127.0.0.1:5555/events/${event.id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: name,
        date_time: dateTime,
        description: description
    })
    })
    .then(response => response.json())
    .then(updateEvent)
  }

  function handleAttend() {
    fetch(`http://127.0.0.1:5555/events/${event.attending_count}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({attending_count: attendingCount})
    })
    removeEvent(event.id)
  }

  return (
    <li className="card">
      {/* <img src={event.image} alt={event.name} />  */}
      <h4>{event.name}</h4>
      <p>When: {event.date_time}</p>
      <p>{event.description}</p>

      {/* NEED (Terenary?) LOGIC TO SHOW 'I WANT TO ATTEND vs. HOST' BASED ON IF YOU ARE A USER OR VENUE */}
      <button onClick={handleAttend} className="attend-event" value={attendingCount} onChange={(e) => setAttendingCount={e.target.value}}></button>

      <button onClick={handleDelete} className="remove-event">Delete Event</button>

        <h2>Update Event</h2>
        <form onSubmit={handleUpdateSubmit}>
            <input type="text" name="name" placeholder="Update Event name" value={name} onChange={(e) => setName(e.target.value)}/>
            <input type="text" name="dateTime" placeholder="Update Date and Time of Event" value={dateTime} onChange={(e) => setDateTime(e.target.value)}/>
            <input type="text" name="description" placeholder="Update Description of Event (100 Chars Max)" value={description} onChange={(e) => setDescription(e.target.value)}/>

            <button type="submit">Add Event</button>
        </form>
    </li>
  );
}

export default EventCard;