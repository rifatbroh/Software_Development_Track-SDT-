const num = [10, 20, 30];

const sq = num.map(el => el * el);
console.log(sq);

/**
 * using for each
 */
num.forEach(element => {
    console.log(element*element);
});
num.forEach(el => {
    console.log(el * el);
});