#!/usr/bin/node

const args = process.argv;
let factorial = 1;

if (isNaN(Number(args[2])) || Number(args[2]) === 0) {
  factorial = 1;	
} else {
	for (i = Number(args[2]); i > 0; i--) {
	  factorial *= i;
	}
}
console.log(factorial);
