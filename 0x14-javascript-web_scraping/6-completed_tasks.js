#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const finished = {};
    todos.forEach((task) => {
      if (task.completed && finished[task.userId] === undefined) {
        finished[task.userId] = 1;
      } else if (task.completed) {
        finished[task.userId] += 1;
      }
    });
    console.log(finished);
  }
});
