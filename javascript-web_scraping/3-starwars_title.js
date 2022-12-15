#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');

const id = process.argv[2];
const uri = 'https://swapi-api.hbtn.io/api/films/' + id;

request.get(uri, (err, res, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
