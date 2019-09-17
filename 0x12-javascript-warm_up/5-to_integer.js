#!/usr/bin/node
const argv = require('process').argv;

let myVar;
const myNumber = parseInt(argv[2]);

if (isNaN(myNumber)) {
  myVar = 'Not a number';
} else {
  myVar = myNumber;
}
console.log(myVar);
