#!/usr/bin/node
const argv = require('process').argv;

const request = require('request');
request(argv[2], function (error, response, body) {
  try {
    console.log('code:', response.statusCode);
  } catch (e) {
    console.log(error);
  }
});
