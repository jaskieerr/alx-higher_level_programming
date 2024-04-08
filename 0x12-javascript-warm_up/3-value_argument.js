#!/usr/bin/node

const argTbp = process.argv[2];

if (argTbp === null) {
  console.log('No argument');
} else {
  console.log(argTbp);
}
