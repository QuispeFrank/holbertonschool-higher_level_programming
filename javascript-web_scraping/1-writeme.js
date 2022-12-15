#!/usr/bin/node
// script that writes a string to a file.

const fs = require('fs');

const pathFile = process.argv[2];
const text = process.argv[3];

fs.writeFile(pathFile, text, (err) => {
  if (err) throw err;
});
