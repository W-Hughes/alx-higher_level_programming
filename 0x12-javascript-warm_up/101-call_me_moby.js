#!/usr/bin/node
// This module exports a function that executes a given function x number of times.

exports.callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
