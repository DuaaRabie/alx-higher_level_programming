#!/usr/bin/node

const process = require('process');

if (process.argv[2]) {
	const converted = Number(process.argv[2]);

	if (!isNaN(converted)) {
		console.log("My number:", converted);
	} else {
		console.log('Not a number');
	}
}
