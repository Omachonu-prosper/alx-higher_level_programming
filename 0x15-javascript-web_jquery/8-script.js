// URL for fetching movie data
var apiUrl = "https://swapi-api.alx-tools.com/api/films/?format=json";

// Select the unordered list with id 'list_movies'
var movieList = $("#list_movies");

// Make an AJAX request to fetch movie data
$.ajax({
    url: apiUrl,
    method: "GET",
    dataType: "json",
    success: function (data) {
        // Iterate through the movies and add their titles to the list
        $.each(data.results, function (index, movie) {
            var movieTitle = movie.title;
            // Create a list item and append it to the 'movieList' ul
            var listItem = $("<li>").text(movieTitle);
            movieList.append(listItem);
        });
    },
    error: function () {
        // Handle any errors here
        movieList.append("<li>Failed to fetch movie data.</li>");
    }
});