#!/usr/bin/node
const argv = require('process').argv;

let myVar;

if (argv.length - 2 === 0) {
  myVar = 'No argument';
} else if (argv.length - 2 === 1) {
  myVar = 'Argument found';
} else {
  myVar = 'Arguments found';
}
console.log(myVar);
