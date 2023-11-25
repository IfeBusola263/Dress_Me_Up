/**
 * This script manages the display of dress images based on the selected event.
 * @file This file contains the dressCatalog object and the displayDress function.
 * @summary The dressCatalog object stores dress images for different events, and the displayDress function handles the logic for displaying the dress images based on the selected event.
 * @requires jQuery
 */

// FILEPATH: /Dress_Me_Up/web_static/scripts/catalog.js
// This is the dressCatalog object that contains dress images for different events.
const dressCatalog = {
    wedding: [
        'wedding.webp',
        'image2.jpg'
    ],
    date: [
        'image3.jpg',
        'image4.jpg'
    ],
    reunion: [
        'image5.jpg',
        'image6.jpg'
    ],
    dinner: [
        'image7.jpg',
        'image8.jpg'
    ],
    birthday: [
        'image9.jpg',
        'image10.jpg'
    ]
};

/**
 * Displays dress images based on the selected event.
 */
function displayDress() {
    const select = $('#events');
    const dressCatalogue = $('#dressCatalogue');

    select.on('change', function () {
        const selectedEvent = this.value;

        dressCatalogue.empty();
        if (dressCatalog[selectedEvent]) {
            dressCatalog[selectedEvent].forEach(image => {
                const img = $('<img>');
                img.attr('src', '/images/' + image);
                dressCatalogue.append(img);
            });
        noDressesMessage.hide(); // Hide the message when dresses are available
        } else {
            dressCatalogue.empty();
            noDressesMessage.show(); // Show the message when no dresses are available
            // dressCatalogue.html('<p class="no-dresses-message">No dresses available for this event.');
        }
    });
}

$(document).ready(function () {
    displayDress();
});
