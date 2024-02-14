#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let elcount = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      elcount += 1;
    }
  }
  return elcount;
};
