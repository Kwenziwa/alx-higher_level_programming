#!/usr/bin/node

const req = require("request");
const url = process.argv[2];

req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const accomplished = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (accomplished[task.userId] === undefined) {
          accomplished[task.userId] = 1;
        } else {
          accomplished[task.userId]++;
        }
      }
    }
    console.log(accomplished);
  } else {
    console.log("An error occured. Status code: " + response.statusCode);
  }
});
