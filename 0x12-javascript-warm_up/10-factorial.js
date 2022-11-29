#!/usr/bin/node

function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const args = process.argv.slice(2);
const num = parseInt(args[0]);
if (isNaN(num)) {
  console.log('1');
} else {
  console.log(factorial(num));
}
