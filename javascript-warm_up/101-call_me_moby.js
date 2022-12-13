#!/usr/bin/node
// function that executes x times a function.

exports.callMeMoby = function (x, theFunction) {
  for (let counter = 0; counter < x; counter++) {
    theFunction();
  }
};
