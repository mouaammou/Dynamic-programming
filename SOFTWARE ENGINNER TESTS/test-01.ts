function average(numbersArray: number[], limitLength: number): number {
    let sum = 0;
    let i;
    for(i = 0; i < limitLength; i++) {
        sum += numbersArray[i];
    }
    console.log("average: ", sum/i);
    return sum/i;
}

function countResponseTimeRegressions(responseTimes: number[]): number {
    // Write your code here
    let greaterAverage = 0;
    for (let i = responseTimes.length - 1; i >= 0; i--) {
        if (i == 0)
            break;
        if (responseTimes[i] > average(responseTimes, i))
            greaterAverage++;
    }

    return greaterAverage;
}

console.log(countResponseTimeRegressions([100, 200, 150,300]));