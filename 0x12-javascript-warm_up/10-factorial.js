#!/usr/bin/node
// This script computes and prints a factorial.

function factorial (number) {
  return (isNaN(number) || number === 0)
    ? 1
    : number * factorial(number - 1);
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
