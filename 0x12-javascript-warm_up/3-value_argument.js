#!/usr/bin/node
const argv = require('process').argv;

let myVar;

if (argv[2] === undefined) {
  myVar = 'No argument';
} else {
  myVar = argv[2];
}
console.log(myVar);
