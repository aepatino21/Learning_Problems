/*
Un  profesor  desea  saber  qué  porcentaje  de  hombres  y  que  porcentaje  de  mujeres  hay  en  un  grupo  de  
estudiantes.
*/

// function to calculate the percentage of men and women in a student group
function studentPercentage(sameSexNumber, totalStudents) {
    let result = ((sameSexNumber / totalStudents) * 100).toFixed(2);
    return Number(result);
}


// find out the number of men and women in the student group
const totalMen = Number(prompt("Enter the number of men in the student group:"));
const totalWomen = Number(prompt("Enter the number of women in the student group:"));

// calculate the percentage of men and women in the student group
const totalStudents = totalMen + totalWomen;
let totalPercentageMen = studentPercentage(totalMen, totalStudents);
let totalPercentageWomen = studentPercentage(totalWomen, totalStudents);
console.log(`The percentage of men is: ${totalPercentageMen} and the percentage of women is: ${totalPercentageWomen}`);