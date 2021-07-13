var combinationSum = function(candidates, target) {
  const ans = [];
  const dfs = (target, combine, idx) => {
      if (idx === candidates.length) {
          return;
      }
      if (target === 0) {
          ans.push(combine);
          return;
      }
      // 直接跳过
      dfs(target, combine, idx + 1);
      // 选择当前数
      if (target - candidates[idx] >= 0) {
          dfs(target - candidates[idx], [...combine, candidates[idx]], idx);
      }
  }

  dfs(target, [], 0);
  return ans;
};
// console.log(combinationSum([1,2,3], 5));

function ways2sum(m, k) {
  // const bases = 1;
  const paths = [];

  const iter = (rest, max, acc) => {
    if (rest  === 0) {
      return
    }
    if (paths[acc] === undefined) {
      paths[acc] = [];
    }
    console.log('rest: ', rest)
    console.log('max: ', max)
    
  }

  iter(m, k, 0)

  return paths;
}

console.log(ways2sum(5))

// given 5, 3,

(p q)**5

Np**3

function way2sum(m, n) {
  let candiates = [1...n];
  1, 1, 1, 1, 1
  1, 2, 2
  3, 2
  3, 1, 1
  2, 1, 1, 1
  function iter(arr, cur) {
    if (arr.sum + cur <= m) {
      arr.push(cur)
    }
    iter(arr, n.first);
    iter(arr, n.second);
  }
}

