#!/usr/bin/node
// script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const dict = require('./101-data').dict;
const newdic = {};

for (const key in dict) {
  if (newdic[dict[key]] === undefined) {
    newdic[dict[key]] = [key];
  } else {
    newdic[dict[key]].push(key);
  }
}

console.log(newdic);
