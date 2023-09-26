#!/usr/bin/node

const the_request = require("request");

const movieId = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;


if (!movieId) {
  console.error("Usage: node get_star_wars_movie.js <movie_id>");
  process.exit(1);
}

the_request(apiURL, (error, response, body) => {
  if (error) {
    console.error(`An error occurred: ${error}`);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(`Title: ${movieData.title}`);
    } else {
      console.error(`request failed with status code ${response.statusCode}`);
    }
  }
});
