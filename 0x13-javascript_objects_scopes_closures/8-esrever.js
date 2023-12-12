#!/usr/bin/node
exports.esrever = function (list) {
  let output = [];
  while (list.length) {
    output.push(list.pop());
  }
  return output;
};
