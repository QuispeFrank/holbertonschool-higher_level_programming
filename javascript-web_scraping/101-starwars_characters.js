#!/usr/bin/node
// script that prints all characters of a Star Wars movie part 2.

const request = require('request');

const movieId = process.argv[2];
const movieUri = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let linksNombres;

request.get(movieUri, (err, res, body) => {
  if (err) throw err;
  linksNombres = JSON.parse(body).characters;
  GetNames().then(innerNames => {
    innerNames.forEach((name) => {
      console.log(name);
    });
  }).catch(err => {
    console.error(err);
  });
});

/* function that allows me to do asynchronous https requests */
async function GetNames () {
  const innerNames = [];
  for (const linkNombre of linksNombres) {
    const response = await new Promise((resolve, reject) => {
      request.get(linkNombre, (err, res, body) => {
        if (err) { reject(err); } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
    innerNames.push(response);
  }
  return innerNames;
}
