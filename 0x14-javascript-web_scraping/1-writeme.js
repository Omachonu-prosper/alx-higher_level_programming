#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: node writefile.js <file_path> "<string_to_write>"');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    // Handle the error by printing the error object
    console.error(err);
  }
});

