#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let square = 0; square < size; square++) {
    let row = '';
    for (let column = 0; column < size; column++) { row += 'X'; }
    console.log(row);
  }
}
