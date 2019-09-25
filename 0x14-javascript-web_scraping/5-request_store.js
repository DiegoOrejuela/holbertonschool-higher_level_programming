#!/usr/bin/node
const argv = require('process').argv;
const fs = require('fs');
const request = require('request');
request(argv[2], function (error, response, body) {
  try {
    fs.writeFile(argv[3], body, 'utf-8', function (err) {
      if (err) { console.log(err); }
    });
  } catch (e) {
    console.log(error);
  }
});
