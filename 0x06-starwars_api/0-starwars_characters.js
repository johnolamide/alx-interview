#!/usr/bin/env node
const request = require('request');

const getCharacterName = (url) => {
  request(url, (error, response, body) => {
    if (!error && response.statusCode == 200) {
      console.log(JSON.parse(body).name);
    }
  });
}

function getCharactersOfMovie(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}`;
  request(url, function(error, response, body){
    if (!error && response.statusCode == 200) {
      const characters = JSON.parse(body).characters;
      for (let i = 0; i < characters.length; i++) {
        getCharacterName(characters[i]);
      }
    }
  });
}

const movieId = process.argv[2];
getCharactersOfMovie(movieId);
