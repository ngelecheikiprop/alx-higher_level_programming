#!/usr/bin/node
const argvLen = process.argv.length;
if (argvLen <= 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
