#!/usr/bin/node
function factorial (a_n) {
  return a_n === 0 || isNaN(a_n) ? 1 : a_n * factorial(a_n - 1);
}

console.log(factorial(Number(process.argv[2])));
