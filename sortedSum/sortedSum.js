const least = 4;
function miniMaxSum(arr) {
    const sums = [];
    const sum_iter = (rest, acc_count, acc) => {
      console.log('acc: ', acc);
      console.log('rest: ', rest);
        if (acc_count === 0) {
            console.log('---finshed---: ', acc);
            sums.push(acc)
            return;
        }
        // acc += 
        const first = rest[0];
        sum_iter(rest.slice(1), acc_count - 1, acc + first)
        if (rest.length - acc_count > 0) {
            sum_iter(rest.slice(1), acc_count, acc)
        }
    }
    sum_iter(arr, least, 0);
    let min_sum = sums[0];
    let max_sum = sums[0];
    for (let sum of sums) {
        if (sum < min_sum) {
            min_sum = sum
        } else if (sum > max_sum) {
            max_sum = sum
        }
    }
    console.log('sums: ', sums)
    console.log(min_sum + '  ' + max_sum)
}
miniMaxSum([7, 69, 2, 221, 8974])