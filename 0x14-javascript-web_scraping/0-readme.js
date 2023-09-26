#!/usr/bin/node
const fs = require('fs');

// Check if the file path argument is provided
if (process.argv.length !== 3) {
  console.error('Usage: node readfile.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read the file content in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Handle the error by printing the error object
    console.log(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
