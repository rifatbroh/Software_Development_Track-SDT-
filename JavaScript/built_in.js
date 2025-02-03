const arr = [22, 30, 39];

// for (let i=0; i<arr.length; i++) {
//     if (arr[i] == 30) {
//         return 30;
//     }
// }

const find_me = (arr, id) => {
    for (let i=0; i<arr.length; i++) {
        if (arr[i] == id) {
            return arr[i];
        }
    }
}
console.log(find_me(arr, 39));

// use built in function 

const res = arr.find(el => el == 39);
console.log(res);
