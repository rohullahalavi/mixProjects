
//sorting numbers algorithm in typescript 
//https://www.typescriptlang.org/docs/handbook/basic-types.html
//https://www.typescriptlang.org/docs/handbook/advanced-types.html
//https://www.typescriptlang.org/docs/handbook/basic-types.html#string-types

//list of unsorted numbers 0..100
let numbers: number[ ] = [ ];
for (let i = 0; i < 100; i++) {
    numbers.push(Math.floor(Math.random() * 100));
}

function sort(numbers: number[ ]): number[ ] {
    let sortedNumbers: number[ ] = [ ];
    while (numbers.length > 0) {
        let lowest = numbers[ 0 ];
        let lowestIndex = 0;
        for (let i = 1; i < numbers.length; i++) {
            if (numbers[ i ] < lowest) {
                lowest = numbers[ i ];
                lowestIndex = i;
            }
        }
        sortedNumbers.push(numbers.splice(lowestIndex, 1)[ 0 ]);
    }
    return sortedNumbers;
}


console.log(sort(numbers));



