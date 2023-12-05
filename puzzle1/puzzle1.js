// import fs from 'fs';

const fs = require('fs'); // it works, so 'require' syntax is available, 'import' will need a 'type':'module' in the package.json or 
// .mjs file extension to work

const countFloor = (path) =>{
  let floor = 0;
  const firstBasmtEntering = [];
  const input_string = fs.readFileSync(path, 'utf8') // readFileSync return the contents of the path
  // it's important to specify an encoding option, after the path,as by default it will return a buffer.
  // Also, I have chosen the synchronous function for the sake of simplicity and readability,therefore avoided unnecessary instructions for promises.
  for (let i = 0; i < input_string.length; i += 1) {
    const bracket = input_string[i];
    if (bracket === '(') {
      floor += 1;
    } else if (bracket === ')') {
      floor -= 1;
    } 
  //part 2: find the position of the first character that causes to go negative
    if (firstBasmtEntering.length < 1 && floor == -1) { //though this works fine, we still have a lot of unnecessary operations,
      // like checking the length of the array, we can use a some() method of an array, but with a separate loop/function (not sure if it's more efficient)
      firstBasmtEntering.push(i + 1) // + 1 because of the task
    }
  }
  return { floor, firstBasmtEntering };
};

console.log(countFloor('./puz1-1.txt'));