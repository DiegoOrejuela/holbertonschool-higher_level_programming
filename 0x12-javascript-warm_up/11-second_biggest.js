#!/usr/bin/node

const argv = require('process').argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const myList = [];
  for (let i = 2; i < argv.length; i++) {
    myList.push(parseInt(argv[i]));
  }
  myList.sort(function (a, b) { return b - a; });
  console.log(myList[1]);
}
