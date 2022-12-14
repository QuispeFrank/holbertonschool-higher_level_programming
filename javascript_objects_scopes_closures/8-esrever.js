#!/usr/bin/node
// function that returns the reversed version of a list.

exports.esrever = function (list) {
  const array = [];
  list.forEach(function reverse (element) { array.unshift(element); });
  return array;
};
