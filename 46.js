/**
 * @param {number[]} nums
 * @return {number[][]}
 */

function dfs(nums, depth, path, used, result) {
    if(depth === nums.length) {
        result.push(path.slice());
        return;
    }
    for(let i = 0; i < nums.length; i++) {
        if(!used[i]) {
            path.push(nums[i]);
            used[i] = true;
            dfs(nums, depth+1, path, used, result);
            used[i] = false;
            path.splice(path.length-1, 1);
        }
    }
}

var permute = function(nums) {
    var result = [];
    if(nums.length == 0) {
        return result;
    }
    
    var used = []
    for(let i = 0; i < nums.length; i++) {
        used[i] = false;
    }
    var path = [];
    dfs(nums, 0, path, used, result);
    return result;
};
