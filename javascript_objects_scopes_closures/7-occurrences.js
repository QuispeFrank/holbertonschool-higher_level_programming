#!/usr/bin/node
// function that returns the number of occurrences in a list.

exports.nbOccurences = function (list, searchElement) {
  const foundE = list.filter(function checkEqual (value) { return value === searchElement; });
  return foundE.length;
};
