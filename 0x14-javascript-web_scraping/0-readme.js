#!/usr/bin/node
// reads and prints the content of a file.

const filePath = process.argv[2];
const fs = require('fs');

fs.readFile(filePath, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
