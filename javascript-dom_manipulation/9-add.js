#!/usr/bin/node
const first = process.argv[2];
const second = process.argv[3];

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(first, second));
