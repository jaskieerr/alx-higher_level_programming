#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const parsed = JSON.parse(body).results;
    console.log(parsed.reduce((attandance, films) => {
      return films.characters.find((character) => character.endsWith('/18/'))
        ? attandance + 1
        : attandance;
    }, 0));
  }
});
