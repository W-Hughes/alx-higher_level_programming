#!/usr/bin/node
// This script increments and calls a function.

exports.addMeMaybe = (number, theFunction) => {
  theFunction(number + 1);
};
