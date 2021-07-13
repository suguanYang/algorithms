function quickSortRec(nums) {
  const quickSort = (arr) => {
      if (arr.length <= 1) {
        return arr
      }
      const pivot = arr[0];
      const left = [], right = [];
      for (let n of arr.slice(1)) {
        if (n <= pivot) {
          left.push(n);
        } else {
          right.push(n);
        }
      }
      return quickSort(left).concat(pivot).concat(quickSort(right));
  }

  return quickSort(nums)
}

// console.log(quickSortRec([2,3,1,56,2,2,5,7,299,8,9,0,100]));

function quickSortIter(nums) {
  const parition = (l, h) => {
    const pivotValue = nums[h];
    let pivotIndex = l; 
    console.log('pivotIndex: ', pivotIndex);
    for (let i = l; i < h; i++) {
        if (nums[i] < pivotValue) {
          // Swapping elements
          [nums[i], nums[pivotIndex]] = [nums[pivotIndex], nums[i]];
          // Moving to next element
          pivotIndex++;
        }
    }

    // Putting the pivot value in the middle
    [nums[pivotIndex], nums[h]] = [nums[h], nums[pivotIndex]] 
    console.log('pivotIndex: ', pivotIndex);
    console.log('pivotValue: ', pivotValue);
    console.log('nums: ', nums);
    return pivotIndex;
  }
  const quickSort = (l, h) => {
      if (l >= h) {
        return;
      }

      let p = parition(l, h);
      quickSort(l, p - 1);
      quickSort(p + 1, h);
  }



  quickSort(0, nums.length - 1);
  return nums;
}

console.log(quickSortIter([2,2,0,1]));

// 2, 2, 0, 1: 4
// 1, 2, 0, 2: 1
// 0, 2, 1, 2: 
