#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (err, resp, body) => {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});
