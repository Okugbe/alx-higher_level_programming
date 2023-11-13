#!/usr/bin/node

const userInputCLI = process.argv[2];

if (parseInt(userInputCLI)) {
 for (let i = 0; i < userInputCLI; i++) {
    console.log('C is fun');
 }
} else {
 console.log('Missing number of occurrences'); 
}

