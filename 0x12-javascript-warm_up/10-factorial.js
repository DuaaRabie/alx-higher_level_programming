#!/usr/bin/node

const args = process.argv;

function factorial(n) {
  if (isNaN(n) || n === 0) {
   return (1);	
  } else {
     return (n * factorial(n - 1));
  }
}

console.log(factorial(Number(args[2])));
