#!/usr/bin/node
const argv = require('process').argv;

const request = require('request');
request(argv[2], function (error, response, body) {
  try {
    let count = 0;
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('18')) { count++; }
      }
    }
    console.log(count);
  } catch (e) {
    console.log(error);
  }
});
