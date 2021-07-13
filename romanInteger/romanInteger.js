const romanSymbol2Int = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  let totalV = 0;
  let previousV = 0;
  for (let i in s) {
    let syb = s[i];
    let nextSyb = s[Number(i) + 1];
    const intV = romanSymbol2Int[syb];
    const nextV = romanSymbol2Int[nextSyb]
    if (nextV > intV) {
      previousV = intV;
      continue;
    } else {
      totalV = totalV + intV - previousV;
      previousV = 0;
    }
  }
  return totalV;
};

console.log('IV: ', romanToInt('IV'));
console.log('III: ', romanToInt('III'));
console.log('IX: ', romanToInt('IX'));
console.log('LVIII: ', romanToInt('LVIII'));
console.log('MCMXCIV: ', romanToInt('MCMXCIV'));