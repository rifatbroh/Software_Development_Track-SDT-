/*
    Take input from user, find is it leap year?
*/
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

readline.question("Enter a year: ", (year) =>{
    year = parseInt(year);

    if ((year%4 == 0 && year%100 != 0) || year%400 == 0)
        console.log(`${year} is a leap year`);
    else 
        console.log(`${year} is not a leap year`);

    readline.close();
});