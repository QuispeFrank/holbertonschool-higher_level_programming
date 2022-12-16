#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');

const uri = process.argv[2];
const dic = {};

request.get(uri, (err, res, body) => {
  if (err) throw err;
  const todos = JSON.parse(body);
  todos.forEach((obj) => {
    if (obj.completed === true) {
      if (dic[String(obj.userId)] === undefined) {
        dic[String(obj.userId)] = 1;
      } else {
        dic[String(obj.userId)] = dic[String(obj.userId)] + 1;
      }
    }
  });
  console.log(dic);
});
