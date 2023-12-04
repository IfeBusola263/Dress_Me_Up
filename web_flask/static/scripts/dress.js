/*function showMatchingEvents(dressId, eventList, dressPix) {

    // List for the named dress
    let evenList = []

    // loop through a list of dictionary representation of the events objects
    eventList.forEach((event) => {
	if (dressId === event['dress_id'])
	    evenList.push(event['name'])
    });

    // create a new paragraph and image elements to displays the events and dress
    
    document.getElementById('matchingEvents').innerHTML = `<p>Matching Events: ${evenList.join(', ')}</p>`;
    document.getElementById('matchingEvents').innerHTML = `<img src=${dressPix} alt="Image not available"`
}
$(document).ready(function() {
    function showMatchingEvent() {
        $("a[class='anchor']").on("click", function (event) {
            event.preventDefault(); // Prevent default link behavior
            
            const eventName = $(this).parent().data("name");
            const dressImage = $(this).parent().data("image");
	    const path = dressImage
	    const filename = path.substring(path.lastIndexOf('/') + 1);
           
	    $("#matchingEvents").empty();
	    $("#matchingEvents").append(`<li>${eventName}</li>`);

	    $.ajax({
		type: 'GET',
		url: `upload_dress/${filename}`,
		success: function (data) {
	            $("#matchingEvents").append(`<div><img src="${data}" alt="Dress Image"></div>`);
		},
		error: function () {
		    console.log("No data")
		}
	    });
	    
        });
    }

    showMatchingEvent();
});*/

$(document).ready(function() {
    function showMatchingEvent() {
        $("a[class='anchor']").on("click", function (event) {
            event.preventDefault();

            const dressImage = $(this).parent().data("image");
	    const fileName = dressImage.split('/').pop();

            $.ajax({
                type: 'GET',
                url: `/upload_dress/${fileName}`,
                xhrFields: {
                    responseType: 'blob' 
                },
                success: function (data) {
                    const imageUrl = URL.createObjectURL(data);// Create object URL from blob data
                    $("#matchingEvents").empty();
                    $("#matchingEvents").append(`<div><img src="${imageUrl}" alt="Dress Image"></div>`);
                },
                error: function () {
                    console.log("Error retrieving image");
                }
            });
        });
    }

    showMatchingEvent();
});

