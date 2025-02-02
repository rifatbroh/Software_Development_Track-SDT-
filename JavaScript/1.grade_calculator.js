/*
    calculate your grade
*/
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question("Enter the Student score: ", (score) => {
    let n;
    score = parseInt(score);

    if (score >= 80)
        n = "A+";
    else if (score >= 70)
        n = "A";
    else if (score >= 60)
        n = "A-";
    else if (score >= 50)
        n = "B";
    else if (score >= 40)
        n = "C";
    else
        n = "F";

    console.log(`The grade for a score of ${score} is: ${n}`); // Corrected line
    readline.close();
});