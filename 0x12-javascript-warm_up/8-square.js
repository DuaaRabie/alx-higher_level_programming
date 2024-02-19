#!/usr/bin/node

const args = process.argv;
const size = Number(args[2]);
let square = '';

if (size) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    if (i !== size - 1) {
      square += '\n';
    }
  }
  console.log(square);
} else {
  console.log('Missing size');
}
