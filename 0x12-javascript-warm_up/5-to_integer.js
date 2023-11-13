#!/usr/bin/node

const ArgOne = process.argv[2];
const treatArgOne = parseInt(ArgOne);

if (!ArgOne || isNaN(treatArgOne)) {
  console.log('Not a Number');
} else {
  console.log('My number:', treatArgOne);
}
