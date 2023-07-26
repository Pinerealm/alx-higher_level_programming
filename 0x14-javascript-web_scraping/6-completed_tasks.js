#!/usr/bin/node
// Prints the number of completed tasks by user id.

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const dict = {};

    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed) {
        if (dict[tasks[i].userId]) {
          dict[tasks[i].userId]++;
        } else {
          dict[tasks[i].userId] = 1;
        }
      }
    }
    console.log(dict);
  }
}
);
