#!/usr/bin/node

const args = process.argv;

if (args[2]) {
  const first = Number(args[2]);
  if (!isNaN(first)) {
    for (let i = 0; i < first; i++) {
    console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
}
