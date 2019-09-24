#!/usr/bin/node
const fs = require('fs');
const argv = require('process').argv;

fs.readFile(argv[2], 'utf8', (err, data) => {
  try {
    process.stdout.write(data);
  } catch (e) {
    console.log(err);
  }
});
