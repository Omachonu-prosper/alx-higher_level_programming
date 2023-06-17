#!/usr/bin/node

const argv = process.argv;
const x = Number(argv[2]);

if (x) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
