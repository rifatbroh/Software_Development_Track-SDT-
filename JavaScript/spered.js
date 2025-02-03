const person = {
    name: "rifat hossain",
    id : 39,
    University: "BAIUST",
    campus: "cumilla",
    dept: "CSE",

    /*
        Method declaring
    */
    get_name() {
        return this.name
    },
    get_id() {
        return this.id
    },
    get_university() {
        return this.University
    },
    get_campus() {
        return  this.campus
    }, 
    get_dept() {
        return this.dept
    }
}

console.log(person.get_name());
console.log(person.get_id());
console.log(person.get_university());
console.log(person.get_campus());
console.log(person.get_dept());

const a = [1, 2, 3]
const newArray = {new: "New Property", ...person}
console.log(newArray);

// distrucature

const [first, second] = a;
console.log(first + " " + second);

const {name, id} = person;
console.log(name + " " + id);