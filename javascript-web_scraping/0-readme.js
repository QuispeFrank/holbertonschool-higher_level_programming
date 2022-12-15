#!/usr/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');

const pathFile = process.argv[2];

fs.readFile(pathFile, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
