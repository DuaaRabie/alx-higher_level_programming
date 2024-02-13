#!/usr/bin/node

const args = process.argv;
let first = Number(process.argv[2]);

if (first) {
	while (first) {
		console.log("C is fun");
		first = first - 1;
	}
} else {
	console.log("Missing number of occurrences");
}
