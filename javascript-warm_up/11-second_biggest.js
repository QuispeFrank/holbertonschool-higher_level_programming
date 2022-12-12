#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const array = process.argv.slice(2).sort(function (a, b) { return a - b; });

if (array.length >= 2) {
  console.log(array[array.length - 2]);
} else {
  console.log(0);
}
