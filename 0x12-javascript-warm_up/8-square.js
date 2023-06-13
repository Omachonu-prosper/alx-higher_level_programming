#!/usr/bin/node

const argv = process.argv;
const len = Number(argv[2]);

if (len) {
  for (let i = 0; i < len; i++) {
    let str = '';
    for (let j = 0; j < len; j++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
