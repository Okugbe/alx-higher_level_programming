#!/usr/bin/node

exports.callMeMoby = (num, theFunction) => {
  for (let i = 0; i < num; i++) {
    theFunction();
  }
};
