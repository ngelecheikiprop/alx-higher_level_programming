#!/usr/bin/node
const input = process.argv[2]

if (Number(input)) {
  console.log('My number: ',Number(input));
}
else {
  console.log('Not a number');
}
