#!/usr/bin/node
const Square4 = require('./5-square');
class Square extends Square4 {
  charPrint (c) {
    if (c) {
      let text = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          text += c;
        }
        if (i !== this.height - 1) {
          text += '\n';
        }
      }
      console.log(text);
    } else {
      super.print();
    }
  }
}

module.exports = Square;
