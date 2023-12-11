#!/usr/bin/node

function myFactorial (i) {
  if (isNaN(i) || i < 1) {
    return 1;
  } else {
    return i * myFactorial(i - 1);
  }
}
const i = parseInt(process.argv[2]);
console.log(myFactorial(i));
