#!/usr/bin/node
exports.esrever = function (list) {
  const array = [];
  for (let i = 0; list[i]; i++) {
    array.unshift(list[i]);
  }
  return array;
};

