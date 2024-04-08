#!/usr/bin/node

const argu = process.argv[2];

if (isNaN(argu)) {
  console.log('Not a number');
} else {
  console.log('My number:', +argu);
}
