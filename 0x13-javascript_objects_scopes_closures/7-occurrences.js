#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let index = 0;
  for (let count = 0; count < list.length; count++) {
    if (searchElement === list[count]) {
      index++;
    }
  }
  return index;
};
