const alphas = {
  a: 101,
  b: 2,
  c: 3,
  d: 5,
  e: 7,
  f: 11,
  g: 13,
  h: 17,
  i: 19,
  j: 23,
  k: 29,
  l: 31,
  m: 37,
  n: 41,
  o: 43,
  p: 47,
  q: 53,
  r: 59,
  s: 61,
  t: 67,
  u: 71,
  v: 73,
  w: 79,
  x: 83,
  y: 89,
  z: 97,
};

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const caches = Object.create(null);
  let groupIdx = 0;
  const result = [];
  for (let str of strs) {
    const hashKey = str.split('').reduce((acc, s) => acc * alphas[s], 1);
    if (caches[hashKey] === undefined) {
      caches[hashKey] = groupIdx;
      result[groupIdx] = [];
      groupIdx++;
    }

    result[caches[hashKey]].push(str);
  }
  return result;
};

// groupAnagrams(["eat","tea","tan","ate","nat","bat","ac","bd","aac","bbd","aacc","bbdd","acc","bdd"]);

function is2StringSame(a, b) {
  if (a.length !== b.length) {
    return false;
  }
  let haskKeya = 1;
  let haskKeyb = 1;
  for (let s of a) {
    haskKeya *= alphas[s];
  }
  for (let s of b) {
    haskKeyb *= alphas[s];
  }
  console.log('haskKeyb: ', haskKeyb)
  return haskKeya === haskKeyb;
}

console.log(is2StringSame('daczzzzzzzzz', 'daczzzzzzzzz'));