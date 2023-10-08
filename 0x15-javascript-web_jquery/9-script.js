// URL for fetching the translation
var apiUrl = "https://hellosalut.stefanbohacek.dev/?lang=fr";

$(document).ready(function() {
    // Select the div element with id 'hello'
    var helloDiv = $("#hello");

    // Make an AJAX request to fetch the translation
    $.ajax({
        url: apiUrl,
        method: "GET",
        dataType: "json",
        success: function (data) {
            // Display the translation of "hello" in the 'helloDiv'
            // helloDiv.text(data.hello);
            helloDiv.text(data.hello);
        },
        error: function () {
            // Handle any errors here
            helloDiv.text("Failed to fetch translation.");
        }
    });
});