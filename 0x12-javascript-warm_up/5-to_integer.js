#!/usr/bin/node

const myNumArgs = parseInt(process.argv[2]);

if (myNumArgs) {
  console.log(`My number: ${myNumArgs}`);
} else {
  console.log('Not a number');
}
