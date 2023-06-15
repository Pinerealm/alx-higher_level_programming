#!/usr/bin/node
// conactenates two files into a third file
const args = process.argv.slice(2);

const fs = require('fs');
const file1 = fs.readFileSync(args[0], 'utf8');
const file2 = fs.readFileSync(args[1], 'utf8');

fs.writeFileSync(args[2], file1 + file2, 'utf8');
