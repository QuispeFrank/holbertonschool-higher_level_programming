#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

const uri = process.argv[2];
const filename = process.argv[3];

request.get(uri, (err, res, body) => {
  if (err) throw err;

  fs.writeFile(filename, body, (err) => {
    if (err) throw err;
  });
});
