#!/usr/bin/node
function factorial (number) {
  if (number === 0 || isNaN(number)) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}
console.log(factorial(Number(process.argv[2])));
