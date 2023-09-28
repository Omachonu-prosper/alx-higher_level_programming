#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

// Perform a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    process.exit(1);
  } else {
    const jsonBody = JSON.parse(response.body);
    let moviesCount = 0;
    let i = [];
    let j = [];

    for (i of jsonBody.results) {
      for (j of i.characters) {
        const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
        if (j === characterUrl) {
          moviesCount++;
        }
      }
    }

    console.log(moviesCount);
  }
});
