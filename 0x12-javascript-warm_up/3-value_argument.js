#!/usr/bin/node
let count = 2;
if (!(process.argv[count])) {
  console.log('No argument');
} else {
  while (process.argv[count]) {
    console.log(process.argv[count]);
    count++;
  }
}
