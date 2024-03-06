import React from "react";
import EventCard from "./EventCard";

function EventList({ events, removeEvent, updateEvent }) {   
  // console.log(events)

  const eventList = events.map(event => {
    return <EventCard key={event.id} event={event} removeEvent={removeEvent} updateEvent={updateEvent}/>  
  })

  return (
    <ul className="cards">{eventList}</ul>
  );
}


export default EventList;