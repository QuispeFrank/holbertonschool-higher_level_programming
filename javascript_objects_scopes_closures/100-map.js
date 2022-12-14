#!/usr/bin/node
// script that imports an array and computes a new array.

const list = require('./100-data').list;

const newarray = list.map(function (element, index) {
  return element * index;
});

console.log(list);
console.log(newarray);
