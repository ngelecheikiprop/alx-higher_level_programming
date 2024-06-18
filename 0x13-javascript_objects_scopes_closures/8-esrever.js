#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  let reversedList = [];
  for (let i = len - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
}
