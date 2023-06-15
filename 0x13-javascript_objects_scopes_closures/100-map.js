#!/usr/bin/node
const list = require('./100-data').list;

const newArray = list.map((x, index) => x * index);

console.log(list);
console.log(newArray);
