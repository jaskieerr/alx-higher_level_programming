#!/usr/bin/node
// prints Star Wars movie where episode number matches given integer.

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (err, response, body) => {
  if (err) { console.log(err); }
  const jsonBody = JSON.parse(body);
  console.log(jsonBody.title);
});
