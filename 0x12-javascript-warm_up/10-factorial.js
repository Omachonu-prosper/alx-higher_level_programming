#!/usr/bin/node

const argv = process.argv;
const n = Number(argv[2]);

if (n) {
  console.log(factorial(n));
} else {
  console.log(1);
}

function factorial (n) {
  if (n <= 1) {
    return 1;
  }

  return n * factorial(n - 1);
}
