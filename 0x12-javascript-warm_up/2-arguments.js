#!/usr/bin/node
const { argv } = require('process');
const argcc = argv.length;
if (argcc <= 2) {
  console.log('No argument');
} else if (argcc === 3) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
