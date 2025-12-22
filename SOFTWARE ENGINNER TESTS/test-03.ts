
function isAlpha(input: string): boolean {
    const regex = /^[A-Za-z]+$/;
    return regex.test(input);
}


function isAlphabeticPalindrome(code: string): number {
    // Write your code here
   let arrayOfAlpha: string[] = [];
    for (let i = 0; i < code.length; i ++) {
      if (isAlpha(code[i]))
         arrayOfAlpha[i] = code[i];
    }

    if (arrayOfAlpha.length % 2 != 0)
      return 0;
    for (let i = 0; i < code.length /2; i ++) {
      if(code[i] != code[code.length - 1 - i])
         return 0;
    }
    return 1;
}

console.log(isAlphabeticPalindrome("abc123cba"));
 