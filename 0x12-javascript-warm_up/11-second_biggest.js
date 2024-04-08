#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const sortedArgs = args.sort((a, b) => b - a);

if (sortedArgs.length < 2) {
  console.log(0);
} else {
  console.log(sortedArgs[1]);
}
