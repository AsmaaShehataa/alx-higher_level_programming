#!/usr/bin/node
const dict = require('./101-data').dict;
const hDict = {};
for (const key in dict) {
  if (hDict[dict[key]]) {
    hDict[dict[key]].push(key);
  } else {
    hDict[dict[key]] = [key];
  }
}
console.log(hDict);
