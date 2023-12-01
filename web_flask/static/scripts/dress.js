function showMatchingEvents(dressId, eventList, dressPix) {

    // List for the named dress
    let evenList = []

    // loop through a list of dictionary representation of the events objects
    eventList.forEach(event, () {
	if (dressId === event['dress_id'])
	    evenList.push(event['name'])
    });

    // create a new paragraph and image elements to displays the events and dress
    
    document.getElementById('matchingEvents').innerHTML = `<p>Matching Events: ${evenList.join(', ')}</p>`;
    document.getElementById('matchingEvents').innerHTML = `<img src=${dressPix} alt="Image not available"`
}

