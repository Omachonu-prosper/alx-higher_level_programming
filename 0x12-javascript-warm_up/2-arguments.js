#!/usr/bin/node

const argv = process.argv;

if (argv.length < 3) {
  console.log('No arguement');
} else if (argv.length === 3) {
  console.log('Arguement found');
} else {
  console.log('Arguements found');
}
