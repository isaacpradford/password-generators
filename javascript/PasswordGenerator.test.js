// const jest = require("jest");

const PasswordGenerator = require("./PasswordGenerator");

beforeEach(() => {
  jest.resetModules();
});

function containsUppercase(str) {
  return /[A-Z]/.test(str);
}
function containsLowercase(str) {
  return /[a-z]/.test(str);
}
function containsDigit(str) {
  return /\d/.test(str);
}
function containsSymbol(str) {
  return /[!"#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~]/.test(str);
}

test("Test length", () => {
  expect(PasswordGenerator(12).length).toBe(12);
});

test("Test min length", () => {
  const pw = PasswordGenerator(7);
  expect(pw.length).toBe(0);
});

test("Test max length", () => {
  expect(PasswordGenerator(95).length).toBe(0);
});

test("Test password has a capital", () => {
  expect(containsUppercase(PasswordGenerator(10))).toBe(true);
});

test("Test password has a lowercase", () => {
  expect(containsLowercase(PasswordGenerator(10))).toBe(true);
});

test("Test password has a symbol", () => {
  expect(containsSymbol(PasswordGenerator(10))).toBe(true);
});

test("Test password has a number", () => {
  expect(containsDigit(PasswordGenerator(10))).toBe(true);
});

test("Test character uniqueness", () => {
  const characterSet = new Set();
  const pw = PasswordGenerator(10);
  for (let i = 0; i < pw.length; i++) {
    characterSet.add(pw.charAt(i));
  }

  expect(characterSet.size === pw.length).toBe(true);
});

test("Test no consecutive characters", () => {
  const pw = PasswordGenerator(10);
  for (let i = 0; i < pw.length - 1; i++) {
    expect(pw.charAt(i) != pw.charAt(i + 1)).toBe(true);
  }
});

test("Test consecutive password duplication", () => {
  const pw1 = PasswordGenerator(10);
  const pw2 = PasswordGenerator(10);
  expect(pw1 == pw2).toBe(false);
});
