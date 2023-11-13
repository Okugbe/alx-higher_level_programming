#!/usr/bin/node
const userInputCLI = process.argv[2];

if (!parseInt(userInputCLI)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < userInputCLI; i++) {
    let y = 0;
    let myVar = '';

    while (y < userInputCLI) {
      myVar = myVar + 'X';
      y++;
    }
    console.log(myVar);
  }
}

