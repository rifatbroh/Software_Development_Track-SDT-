/**
 *  array of object
 *  filter return array []
 */
const product = [
    {id:1, name: "Iphone", price: 100000, color: "Gray"},
    {id:2, name: "Macbook", price: 200000, color: "white"},
    {id:1, name: "camera", price: 1000, color: "black"},
]
// find out using filter
const ans = product.filter(el => el.price>50000)
console.log(ans);