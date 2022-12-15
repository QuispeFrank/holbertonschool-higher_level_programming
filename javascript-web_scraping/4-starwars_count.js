#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const uri = process.argv[2];
let performedMovies = 0;

request.get(uri, (err, res, body) => {
  if (err) throw err;

  const movies = JSON.parse(body).results;
  movies.forEach(findMyActor);
  console.log(performedMovies);
});

function findMyActor (dic) {
  dic.characters.forEach((id) => {
    if (id.search('/18/$') !== -1) { performedMovies++; }
  });
}
