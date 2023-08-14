#!/usr/bin/node
const asize = Math.floor(Number(process.argv[2]));
if (isNaN(asize)) {
  console.log('Missing asize');
} else {
  for (let r = 0; r < asize; r++) {
    let row = '';
    for (let c = 0; c < asize; c++) row += 'X';
    console.log(row);
  }
}
