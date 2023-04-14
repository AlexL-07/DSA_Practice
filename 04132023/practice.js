// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.
var isPalindrome = function(s) {
    if(s.length === 0) return true

    const alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'.split('');
    const alphabetSet = new Set(alphabet);
    let newStr = ""

    for(char of s){
        if(alphabetSet.has(char.toLowerCase())){
            newStr += char.toLowerCase()
        }
    }

    return newStr === newStr.split("").reverse().join("");
};