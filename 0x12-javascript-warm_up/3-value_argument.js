#!/usr/bin/node
const argument = process.argv;

if (typeof(argument[2]) === 'undefined') {
  console.log('undefined');
} else {
  console.log(argument[2]);
}

