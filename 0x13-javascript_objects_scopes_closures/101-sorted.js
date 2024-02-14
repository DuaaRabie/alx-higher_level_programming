#!/usr/bin/node

const dict = require('./101-data').dict;

const newdict = {};

for (const userId in dict) {
  const occur = dict[userId];

  if (!newdict[occur]) {
    newdict[occur] = [];
  }

  newdict[occur].push(userId);
}
console.log(newdict);
