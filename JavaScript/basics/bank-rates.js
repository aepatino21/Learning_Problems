/*
Suponga que un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganara después 
de un mes si el banco paga a razón de 2% mensual. 
*/

// function to calculate how much money the client will make at the end of the month
function calculateRates(capital) {
    const rate = 0.02;
    return capital * rate;
}


let clientCapital = prompt("Enter the capital to invest in our bank:");
console.log(`The client will gain ${calculateRates(clientCapital)} with our monthly 2% rate`);