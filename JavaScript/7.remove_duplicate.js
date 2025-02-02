/*
    Remove duplicate from array
*/
var arr = [1, 2, 3, 3, 5, 5, 5, 9, 9, 10];

var unique= [];
for (var num of arr) {
    if (!unique.includes(num)) {
        unique.push(num);
    }
}
console.log("Unique Numbers: ", unique);