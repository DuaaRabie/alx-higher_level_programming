#!/usr/bin/node

const args = process.argv;

if (args[2]) {
  let first = Number(args[2]);
  if (!isNaN(first)) {
  		while (first) {
    		console.log('C is fun');
    		first = first - 1;
  		}
  } else {
  		console.log('Missing number of occurrences');
  }
}
