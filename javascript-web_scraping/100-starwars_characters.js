#!/usr/bin/node
// script that prints all characters of a Star Wars movie.

const request = require('request');

const movieId = process.argv[2];
const movieUri = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request.get(movieUri, (err, res, body) => {
  if (err) throw err;

  const actorsUri = JSON.parse(body).characters;

  actorsUri.forEach((actorUri) => {
    request.get(actorUri, (err, res, bady) => {
      if (err) throw err;
      const name = JSON.parse(bady).name;
      console.log(name);
    });
  });
});
