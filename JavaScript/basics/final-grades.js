/*
Un alumno desea saber cuál será su calificación final en la asignatura: Introducción a la informática. Dicha 
calificación se compone de los siguientes porcentajes:  
    55% del promedio de sus tres calificaciones parciales.  
    30% de la calificación del examen final.  
    15% de la calificación de un trabajo final.
*/

// function to calculate the final grade
function calculateGrade(partialExams, finalExam, finalProject) {
    let result = ((partialExams / 3) * 0.55) + (finalExam * 0.30) + (finalProject * 0.15);
    return Number(result.toFixed(2));
}


// partial exams grades
const firstPartialExam = Number(prompt("Enter your first partial exam grade:"));
const secondPartialExam = Number(prompt("Enter your second partial exam grade:"));
const thirdPartialExam = Number(prompt("Enter your third partial exam grade:"));

// final exam grade
const finalExam = Number(prompt("Enter your final exam grade:"));

// final project grade
const finalProject = Number(prompt("Enter your final project grade:"));

// show the final grade
let finalGrades = calculateGrade(firstPartialExam + secondPartialExam + thirdPartialExam, finalExam, finalProject);
console.log(`The final grade is: ${finalGrades} pts.`);