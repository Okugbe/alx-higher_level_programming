#!/usr/bin/node 
const ArgOne = process.argv[2];
const number = parseInt(ArgOne);

function calcFactorial(n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * calcFactorial(n - 1);
  }
}

if (!isNaN(number)) {
  console.log(calcFactorial(number));
} else {
  console.log('1');
}
