# Password Generators:
A simple example of a popular practical code exam where the goal is to generate a secure password. My solution is written in 4 languages with tests, just as a small bit of practice for myself.

# Requirements: 
- Generates n length of password
- No duplicate characters
- No two same characters next to each other
- Include special characters, capital letters, lowercase letters, and a number
- Min length of 8

# Solution:
*In passwordgenerator.js*
```
const PasswordGenerator = (length) => {
  let upper = [ "A", ...];
  let lower = ["a", ...];
  let symbol = ["!", ...];
  let digit = ["1", ...];
  let charSet = [upper, lower, digit, symbol];

  let pw = "";

  while (pw.length < length) {
    if (length < 8) return pw; // Ensure minimum length
    if (length > upper.length + lower.length + digit.length + symbol.length)
      return pw; // Ensure maximum length

  // Once charset is empty, re-add the arrays that still have characters
    if (charSet.length === 0) {
      if (upper.length != 0) charSet.push(upper);
      if (lower.length != 0) charSet.push(lower);
      if (digit.length != 0) charSet.push(digit);
      if (symbol.length != 0) charSet.push(symbol);
    }

  // Get random set from charSet
    let setIndex = getRandomInt(0, charSet.length - 1);

  // Get random character from selected set
    let charSetLength = charSet[setIndex].length - 1;
    let charIndex = getRandomInt(0, charSetLength);

  // Add random character to password, remove it and the used charset from their respective arrays
  // This ensures all character types are getting used
    pw += charSet[setIndex][charIndex];
    charSet[setIndex].splice(charIndex, 1);
    // charSet.splice(setIndex, 1);
  }

  return pw;
};
```

My solution is fairly straightforward, and has a simple process. First, the function / class instantiates an Array (or ArrayList in Java) of each of the main character types (Capital, lower, digit, symbol). Then it creates a 2D array that holds each of these charSet arrays and an empty password string. Next, it starts a while-loop that runs until the password string is == the length of the passed in length parameter. It starts by checking to ensure the array holding all 4 arrays isn't empty (and re-adds the charSet arrays if it is), and then picking a random array from the 2D Array and a random character from that array. Last, it adds that selected character to the password string, removes the selected character (guaranteeing no duplicates), removes the character array from the 2D array (guaranteeing all character types get used), and then pushes on until the while loop is over, returning the constructed password at the end.

This solution has an O(n) time where n = the length of the requested password. This solution also is very modular, as it's very easy to change which characters are accepted and which aren't.

# Drawbacks:
1. While this solution is quick and simple, it has a few drawbacks. By removing the character array from the 2D array after it's used once, you're guaranteeing that no 2 consecutive characters are the same character type. This limits the total number of possible outputs.
2. It's currently using each languages generic random libraries. On some of these languages, that's fine, but on others (javascript), the random isn't cryptographically secure, and this could limit the security of the passwords generated.

# Example outputs
1. Eo8\-I9u|5Nq2_KbkZ4,
2. \h5I7U|lQt8"1K:f'q9Y
3. m1J@/2qG8.Xdu,9FPp{0
4. 2fH{w5M!>Z8g.1cNl0@S
5. 9Nr.1A+jqQ"7B4?bZ*c0
6. M=z3nQ-17Tt{(0ZxJ5f[
7. Ms3@rF9,7b^NBw8:a%K1
8. r5=B`6lGV&p2Je@7qZ4"
9. 5?YxSe1=^6Bm.L3vcI8$
10. 3X\a$9gA5,qV*C8es7J}
