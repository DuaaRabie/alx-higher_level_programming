#!/usr/bin/node

const args = process.argv;

if (args.length === 2) {
  console.log(0);
} else if (args.length === 3) {
  console.log(0);
} else {
	let biggest = args[3];
	for (let i = 4; i < args.length; i++) {
	  if (args[i] > biggest) {
	    biggest = args[i];
	  }
	}
        let secbig = args[3];
	for (i = 4; i < args.length; i++) {
	  if (args[i] > secbig && args[i] < biggest)
		secbig = args[i];
	}
	console.log(secbig);
}
