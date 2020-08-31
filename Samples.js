// Function that calculates the sum of all numbers from 1 up to (and including) n.
// Big O(N)

function addUpTo(n) {
    let total = 0;
    for (let i = 1; i <= n; i++) {
        total += i;
    }
    return total;
}

// Function that returns pairs of numbers, starting at 0,0, leading up to just before n,n.
// 0(n^2)
function printAllPairs(n) {
    for (var i = 0; i < n; i++) {
        for (var j = 0; j < n; j++) {
            console.log(i, j);
        }
    }
}