/*
   We want the smallest positive missing integer.

   Start with [3, 4, -1, 1]
   - i=0: value 3 ⇒ swap with index 2 ⇒ [-1, 4, 3, 1]
   - i=0: value -1 is out of range ⇒ move on
   - i=1: value 4 ⇒ swap with index 3 ⇒ [-1, 1, 3, 4]
   - i=1: value 1 ⇒ swap with index 0 ⇒ [1, -1, 3, 4]
   - now 1 at index 0, 3 at 2, 4 at 3; -1 remains at index 1

   Scan from index 0:
   index 0 has 1 (correct), index 1 has -1 (not 2) ⇒ missing positive is 2

 */

function sortTable(numbers: number[]): void {
   const n = numbers.length - 1;
   let swapped: boolean;

   for (let i = 0; i < n; i++) {
      swapped = false;
      for (let j = 0; j < n - i; j++) {
         if (numbers[j] > numbers[j + 1]) {
            [numbers[j], numbers[j + 1]] = [numbers[j + 1], numbers[j]]
            swapped = true;
         }
      };

      if (!swapped) break;
   }
}

function findSmallestMissingPositive(orderNumbers: number[]): number {
   // Write your code here
   sortTable(orderNumbers);
   let smallestNumber = 1;
   for (let i = 0; i < orderNumbers.length; i++) {
      if (orderNumbers[i] == smallestNumber)
      {
         smallestNumber ++;
      }
   }
   return smallestNumber;
}

console.log(findSmallestMissingPositive([1, 2, 3]));
