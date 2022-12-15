#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');

const uri = process.argv[2];

request.get(uri, (err, res, body) => {
  if (err) throw err;
  console.log('code: ' + res.statusCode);
});
