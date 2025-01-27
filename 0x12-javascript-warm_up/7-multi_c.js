#!/usr/bin/node
// This script prints x times "C is fun", where x is an argument of type number.
const x = (process.argv[2]);
if (isNaN(x) || x === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(x); i++) {
    console.log('C is fun');
  }
}
