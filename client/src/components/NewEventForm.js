import React, { useState } from "react";

function NewEventForm({ onNewEventFormSubmit }) {
  const [name, setName] = useState("")
  const [dateTime, setDateTime] = useState("")
  const [description, setDescription] = useState("")

  function handleSubmit(e) {
    e.preventDefault()
    const newEvent = {
        name: name,
        date_time: dateTime,
        description: description
    }
    fetch("http://127.0.0.1:5555/events", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newEvent)
    })
    .then(response => response.json())
    .then(onNewEventFormSubmit)
        setName("")
        setDateTime("")
        setDescription("")
}

  return (
    <div className="new-event-form" onSubmit={handleSubmit}>
      <h2>New Event Form</h2>
      <form>
        <input type="text" name="name" placeholder="Event name" value={name} onChange={(e) => setName(e.target.value)}/>
        <input type="text" name="dateTime" placeholder="Date and Time of Event" value={dateTime} onChange={(e) => setDateTime(e.target.value)}/>
        <input type="text" name="description" placeholder="Brief Description of Event (100 Chars Max)" value={description} onChange={(e) => setDescription(e.target.value)}/>

        <button type="submit">Add Event</button>
      </form>
    </div>
  );
}

export default NewEventForm;