#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;

    let count = 0;
    for (let i = 0; i < films.length; i++) {
      const characters = films[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
}
);
