#!/usr/bin/node
const v = Math.floor(Number(process.argv[2]));
if (isNaN(v)) {
  console.log('A Missing number of occurrences');
} else {
  for (let i = 0; i < v; i++) {
    console.log('C is fun');
  }
}
