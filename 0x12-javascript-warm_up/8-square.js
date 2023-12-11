#!/usr/bin/node

const argvNum = parseInt(process.argv[2]);
// const argvnum2 = process.argv[2]
if (argvNum) {
  for (let i = 0; i < argvNum; i++) {
    console.log('X'.repeat(argvNum));
  }
} else {
  console.log('Missing size');
}
