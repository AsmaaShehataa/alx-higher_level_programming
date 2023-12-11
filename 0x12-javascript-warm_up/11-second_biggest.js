#!/usr/bin/node

const mynum = process.argv;

if (mynum.length <= 3) {
  console.log(0);
} else {
  const args = mynum.slice(2).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
