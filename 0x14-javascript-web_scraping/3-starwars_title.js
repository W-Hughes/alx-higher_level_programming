#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const baseURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(baseURL, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
