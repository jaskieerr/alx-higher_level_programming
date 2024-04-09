#!/usr/bin/node

let naap = 0;

exports.logMe = function (item) {
  console.log(`${naap}: ${item}`);
  naap++;
};
