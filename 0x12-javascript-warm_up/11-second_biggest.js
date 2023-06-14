#!/usr/bin/node

function secondBiggest (list) {
  if (list.length < 2) {
    return 0;
  } else {
    list.sort((a, b) => a - b);
    return list[list.length - 2];
  }
}

const args = process.argv.slice(2);
const list = args.map(x => parseInt(x));
console.log(secondBiggest(list));
