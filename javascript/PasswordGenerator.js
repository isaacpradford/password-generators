// Run with: node PasswordGenerator.js
// Test with: npm test

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

const PasswordGenerator = (length) => {
  let upper = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
  ];
  let lower = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
  ];
  let symbol = [
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
  ];
  let digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
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
    charSet.splice(setIndex, 1);
  }

  return pw;
};

PasswordGenerator(12);

module.exports = PasswordGenerator;
