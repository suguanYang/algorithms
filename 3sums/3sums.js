 var threeSum = function(nums) {
  const dupObjHelper = {};
  nums.sort();
  function iter(acc, curr, rest) {
    // console.log('curr: ', curr)
    console.log('rest: ', rest)
    // console.log('dupObjHelper: ', dupObjHelper)
    if (curr.length === 3) {
      const sum = curr.reduce((a, cur) => a + cur, 0);
      if (sum === 0) {
        acc.push(curr);
      }
      return;
    }

    if (rest.length + curr.length < 3) {
      return;
    }

    const rerest = rest.slice(1);
    dupObjHelper[rest[0]] = true;
    iter(acc, curr.concat(rest[0]), rerest);
    iter(acc, curr, rerest);
  }

  let sum = [];
  iter(sum, [], nums);
  return sum;
};

console.log(threeSum([ -1, -1, -4, 0]))


// var threeSum = function(nums) {
//   const len = nums.length;
//   let acc = [];
//   let donObj = {};
//   nums.sort()
//   function iter(ac, curr, sum) {
//     for (let i = curr+1; i < nums.length; i++) {
//       let diff = sum - nums[i];
//       if (donObj[[nums[i], diff]]) {
//           continue;
//       }
//       let third = undefined;
//       for (let j = i + 1; j < nums.length; j++) {
//         if (nums[j] === diff) {
//           third = nums[j];
//         }
//       }
//       if (third !== undefined) {
//         ac.push([nums[curr], nums[i], diff]);
//         donObj[[nums[i], diff]] = true;
//       }
//     }
//   }

//   for (let q = 0; q < len; q++) {
//     if (donObj[nums[q]]) {
//       continue;
//     }
//     iter(acc, q, 0 - nums[q]);
//     donObj[nums[q]] = true;
//   }
//   return acc;
// };