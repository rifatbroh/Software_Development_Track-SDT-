/*
    Find is it Even or Odd
*/
const readline = require('readline').createInterface ({
    input: process.stdin,
    output: process.stdout,
});

readline.question("Enter a randome Number: ", (n) => {
    n = parseInt(n);

    if (n%2 == 0)
        console.log(`${n} is Even`);
    else
        console.log(`${n} is Odd`);

    readline.close();
});