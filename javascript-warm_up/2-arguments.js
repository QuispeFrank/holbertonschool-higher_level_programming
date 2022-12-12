#!/usr/bin/node
// script that prints the first argument passed to it.

const len = process.argv.length;
let msg = 'No argument';

if (len === 3) {
  msg = 'Argument found';
} else if (len > 3) {
  msg = 'Arguments found';
}
console.log(msg);
