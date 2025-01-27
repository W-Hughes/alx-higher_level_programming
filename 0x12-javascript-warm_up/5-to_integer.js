#!/usr/bin/node
// This script prints My number: <first argument converted in integer>
((isNaN(process.argv[2])) || (process.argv[2] === undefined))
  ? console.log('Not a number')
  : console.log('My number:', parseInt(process.argv[2]));
