// URL for fetching character data
var apiUrl = "https://swapi-api.alx-tools.com/api/people/5/?format=json";

// Select the div element with id 'character'
var characterDiv = $("#character");

// Make an AJAX request to fetch character data
$.ajax({
    url: apiUrl,
    method: "GET",
    dataType: "json",
    success: function (data) {
        // Extract the character name from the fetched data
        var characterName = data.name;

        // Display the character name in the 'characterDiv'
        characterDiv.text("Character Name: " + characterName);
    },
    error: function () {
        // Handle any errors here
        characterDiv.text("Failed to fetch character data.");
    }
});