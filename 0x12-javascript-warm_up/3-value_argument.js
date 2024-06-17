#!/usr/bin/node
const argvLen = process.argv.length;
if (argvLen <= 2) {
  console.log('No argument');
} else {
  let count = 2;
  while (count <= argvLen) {
    console.log(process.argv[count]);
    count++;
  }
}
