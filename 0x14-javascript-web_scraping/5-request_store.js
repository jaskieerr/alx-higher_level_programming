#!/usr/bin/node
const fs = require('fs');
const request = require('request');
url =  process.argv[2];
path = process.argv[3];
request(url).pipe(fs.createWriteStream(path));
