#!/usr/bin/node
// script that concats 2 files.

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

readAndappend(file1, file3);
readAndappend(file2, file3);

function readAndappend (filefrom, fileto) {
  fs.readFile(filefrom, 'utf8', (err, text) => {
    if (err) throw err;
    fs.appendFile(fileto, text.toString(), (err) => {
      if (err) throw err;
    });
  });
}
