/*
    Longest string from array
*/
var friends = ["rahim", "karim", "abdul", "sadsd", "heroalom"];

let longest = "";
for (let name of friends) {
    if (name.length > longest.length) {
        longest = name;
    }
}
console.log(`The longest name is: ${longest}`);