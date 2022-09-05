#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < x; index++) {
    console.log('C is fun');
  }
}
