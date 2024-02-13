#!/usr/bin/node

const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  let biggest = Number(args[2]);
  let secbig = biggest;

  for (let i = 4; i < args.length; i++) {
	  const current = Number(args[i]);

	  if (current > biggest) {
	     secbig = biggest;
	     biggest = current;
	  } else if (current > secbig && current < biggest) {
	    secbig = current;
	  }
  }
  console.log(secbig);
}
