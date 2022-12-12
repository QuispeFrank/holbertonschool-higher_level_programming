#!/usr/bin/node
// script that prints a square

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let times = size; times > 0; times--) {
    console.log('X'.repeat(size));
  }
}
