#!/usr/bin/node
exports.esrever = function (list) {
  const fallingInReverse = [];
  for (let i = list.length - 1; i >= 0; i--) {
    fallingInReverse.push(list[i]);
  }
  return fallingInReverse;
};
