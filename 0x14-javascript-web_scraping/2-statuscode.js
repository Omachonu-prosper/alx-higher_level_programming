#!/usr/bin/node
const request = require('request');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: node get_request_status.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

// Perform a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    console.error('An error occurred while making the GET request:', error);
    process.exit(1);
  } else {
    // Print the status code
    console.log(`code: ${response.statusCode}`);
  }
});
