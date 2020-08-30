// Function that calculates the sum of all numbers from 1 up to (and including) n.
// Big O(N)

function addUpTo(n) {
    let total = 0;
    for (let i = 1; i <= n; i++) {
        total += i;
    }
    return total;
}