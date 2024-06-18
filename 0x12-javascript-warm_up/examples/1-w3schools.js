#!/usr/bin/node
const person = {
    name:['ngelechei', 'kiprop'],
    age: 24,
    bio:function(){
        console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old`);
    },
    introduceSelf:function(){
        console.log(`Hi I'm ${this.name[0]}`)
    }
};
//using dot notation
console.log(person.bio());
console.log(person.introduceSelf());

//using brackets notation
console.log('using brackets notation')
console.log(console.log(person['age']));

//reseting age
console.log('reseting age ...');
person.age = 25;
console.log(`age is now: ${person.age}`);