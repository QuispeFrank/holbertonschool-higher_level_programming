#!/usr/bin/node
// script that prints the addition of 2 integers

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

console.log(add(num1, num2));

function add (a, b) {
  return num1 + num2;
}
