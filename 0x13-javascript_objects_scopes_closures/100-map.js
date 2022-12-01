#!/usr/bin/node
const list = require('./100-data').list;

function map (array, func) {
  const newArray = [];
  for (let i = 0; i < array.length; i++) {
    newArray.push(func(array[i], i));
  }
  return newArray;
}

const newList = map(list, (x, i) => x * i);
console.log(list);
console.log(newList);
