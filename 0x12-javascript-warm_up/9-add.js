#!/usr/bin/node
// This script prints the addition of 2 integer arguments.
function add (a, b) {
  return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
(isNaN(arg1) || isNaN(arg2))
  ? console.log('NaN')
  : console.log(add(arg1, arg2));
