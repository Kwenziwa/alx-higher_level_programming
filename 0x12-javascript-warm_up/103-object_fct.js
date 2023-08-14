#!/usr/bin/node
let myObjects = {
  type: 'object',
  value: 12
};
console.log(myObjects);

myObjects.incr = function () {
  this.value++;
};

myObjects.incr();
console.log(myObjects);
myObjects.incr();
console.log(myObjects);
myObjects.incr();
console.log(myObjects);
