#!/usr/bin/node
const argv = require('process').argv;

const ocurrences = parseInt(argv[2]);

if (isNaN(ocurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < ocurrences; i++) {
    console.log('C is fun');
  }
}
