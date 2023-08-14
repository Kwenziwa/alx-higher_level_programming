#!/usr/bin/node
const anum = Math.floor(Number(process.argv[2]));
console.log(isNaN(anum) ? 'Not a number' : `My number: ${anum}`);
