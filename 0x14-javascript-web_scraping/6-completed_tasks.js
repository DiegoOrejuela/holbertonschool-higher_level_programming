#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');
request(argv[2], function (error, response, body) {
  try {
    const taskCompletedById = {};
    for (const task of JSON.parse(body)) {
      if (task.completed) {
        if (taskCompletedById[task.userId]) {
          taskCompletedById[task.userId] += 1;
        } else {
          taskCompletedById[task.userId] = 1;
        }
      }
    }
    console.log(taskCompletedById);
  } catch (e) {
    console.log(error);
  }
});
