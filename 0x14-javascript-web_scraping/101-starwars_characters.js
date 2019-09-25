#!/usr/bin/node
const argv = require('process').argv;

const request = require('request');
request('http://swapi.co/api/films/' + argv[2], async function (error, response, body) {
  try {
    const film = JSON.parse(body);
    for (const characters of film.characters) {
      function getPromise() {
      return result = new Promise ((resolve, reject) => {
        request(characters, function (error, response, body) {
          try {
            const name = JSON.parse(body).name;
            console.log(name);
          } catch (e) {
            console.log(error);
          }
        });
      });
      }
      await getPromise();
    }
  } catch (e) {
    console.log(error);
  }
});
