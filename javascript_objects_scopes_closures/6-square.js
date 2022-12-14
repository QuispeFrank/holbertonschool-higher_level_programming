#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square.js.

const MainSquare = require('./5-square');

class Square extends MainSquare {
  constructor (side) {
    super(side);
    this.side = side;
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      this.side = this.height;
      for (let grow = 0; grow < this.side; grow++) {
        console.log(c.repeat(this.side));
      }
    }
  }
}
module.exports = Square;
