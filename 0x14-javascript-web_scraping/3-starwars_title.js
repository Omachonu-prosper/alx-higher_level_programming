#!/usr/bin/node
const request = require('request');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: node 3-starwars_title.js <id>');
  process.exit(1);
}

const id = process.argv[2];

// Perform a GET request to the specified URL
request.get('https://swapi-api.alx-tools.com/api/films/' + id, (error, response) => {
  if (error) {
    process.exit(1);
  } else {
    const jsonBody = JSON.parse(response.body);
    console.log(jsonBody.title);
  }
});
