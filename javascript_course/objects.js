const object1={
    message:'Good job',
    price:230
};
const object2={
    message:'Good job',
    price:230
};
const object3= object2;
const object4={
    message:'Good job',
    price:230
};
const {message,price}=object1; //destructing
console.log(message+" "+price); 
const object5={
    message                     // shorthand property
    method(){
        console.log('method')     // shorthand methods
    }
}; 
object5.meyhod();             
console.log('hello'.length);        //autoboxing
console.log('hello'.toUpperCase()); // autoboxing
console.log(object2===object3); // differet reference var but same obj
console.log(object2===object4); // differet reference var different obj 
