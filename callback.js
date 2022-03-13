
//arrow function
var isEven=(ele)=>{
    return ele%2===0;
}

console.log(isEven(2));

//call back function
var result=[2,8,4,4,6].every((e)=> e%2===0);

// when you do not return anythis you must not use {} in call bcak fn

console.log(result);


// this line is added letter