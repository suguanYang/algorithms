/**
 * @param {string} s
 * @return {string}
 */
 var longestPalindrome = function(s) {
    let max = 0;
    let res = s[0];
    if (s.length === 0) {
      return ''
    }
    const iter = (l, r) => {
      if (l < 0 || r >= s.length ) {
        return;
      }
      if (s[l] === s[r]) {
        const sub_s = s.slice(l, r + 1);
        if (max < sub_s.length) {
          max = sub_s.length;
          res = sub_s;
        }
        iter(l - 1, r + 1);
      } else {
        return;
      }
    }

    for (let i = 0; i < s.length; i++) {
      iter(Number(i), Number(i) + 1);
      iter(Number(i) - 1, Number(i) + 1);
    }

    return res;
};

console.log(longestPalindrome('babad'))