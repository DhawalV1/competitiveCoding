/**
 * @param {number[]} nums
 * @return {number}
 */
var countNicePairs = function(nums) {
    
    const mod = 10**9 + 7;
    const modi = [];
    const mapi = {};

    nums.forEach(l => {
        if (l === 0) {
            modi.push(0);
        } else {
            modi.push(l - parseInt(l.toString().split('').reverse().join('').replace(/0+$/, '')));
        }
    });

    modi.forEach(i => {
        if (mapi[i]) {
            mapi[i] += 1;
        } else {
            mapi[i] = 1;
        }
    });

    let sumi = 0;
    for (let key in mapi) {
        sumi += ((mapi[key] - 1) * mapi[key] / 2) % mod;
    }

    return sumi % mod;
};