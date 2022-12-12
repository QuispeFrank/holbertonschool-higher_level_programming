#!/usr/bin/node
// script that prints My number: <first argument converted in integer>

const number = parseInt(process.argv[2]);
let msg = 'My number: ' + number;

if (isNaN(number)) {
  msg = 'Not a number';
}
console.log(msg);
