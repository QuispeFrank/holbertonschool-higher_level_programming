#!/usr/bin/node
// script that prints the first argument passed to it.

const arg = process.argv[2];
const msg = 'No argument';

if (arg !== undefined) {
  console.log(arg);
} else {
  console.log(msg);
}
