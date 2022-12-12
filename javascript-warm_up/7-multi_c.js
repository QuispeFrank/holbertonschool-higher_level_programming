#!/usr/bin/node
// script that prints x times “C is fun”

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let idx = 0; idx < x; idx++) {
    console.log('C is fun');
  }
}
