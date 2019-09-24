#!/usr/bin/node
const argv = require('process').argv;

const request = require('request');
request('http://swapi.co/api/films/' + argv[2], function (error, response, body) {
  try {
    console.log(JSON.parse(body).title);
  } catch (e) {
    console.log(error);
  }
});
