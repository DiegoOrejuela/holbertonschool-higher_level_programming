#!/usr/bin/node
const argv = require('process').argv;

const request = require('request');
request('http://swapi.co/api/films/' + argv[2], function (error, response, body) {
  try {
    const film = JSON.parse(body);
    for (const characters of film.characters) {
      request(characters, function (error, response, body) {
        try {
          console.log(JSON.parse(body).name);
        } catch (e) {
          console.log(error);
        }
      });
    }
  } catch (e) {
    console.log(error);
  }
});
