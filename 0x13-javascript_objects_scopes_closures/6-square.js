#!/usr/bin/node

const mainSquare = require('./5-square.js');

class Square extends mainSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let result = '';

    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        result += c;
      }
      if (i < this.height - 1) {
        result += '\n';
      }
    }
    console.log(result);
  }
}

module.exports = Square;
