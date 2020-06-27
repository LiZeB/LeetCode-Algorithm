/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
// 解法一：没有在递归中全部去重，提交时超出时间限制
var combinationSum2 = function(candidates, target) {
    var result = [];
    if(candidates.length === 0  || target === 0) {
        return;
    }
    candidates.sort((x, y) => {
        if(x < y) {
            return -1;
        } else if(x > y) {
            return 1;
        } else {
            return 0;
        }
    });
   
    var path = [];
    var used = new Array(candidates.length);
    for(let i = 0; i < used.length; i++) {
        used[i] = false;
    }
    dfs(candidates, result, path, used, target);

    var flaged = new Array(result.length);
    for(let i=0; i < flaged.length; i++) {
        flaged[i] = true;
    }

    for(let i=0; i< result.length-1; i++) {
        var string1 = result[i].join();
        for(let j=i+1; j<result.length; j++) {
           if(string1 === result[j].join()) {
                flaged[i] = false;
           }
        }
    }
    var temp = [];
    for(let i = 0; i < flaged.length; i++) {
        if(flaged[i]) {
            temp.push(result[i]);
        }
    }
  
    return temp;
};

function dfs(candidates, result, path, used, target) {
    var sum = 0;
    for(let i = 0; i < path.length; i++) {
        sum = sum + path[i];
    }
    if(sum === target) {
        result.push(path.slice());
        return;
    }
    for(let i = 0; i < candidates.length; i++) {
        if(!used[i]) {
            if(path.length !== 0) {
                if(path[path.length-1] <= candidates[i]) {
                    path.push(candidates[i]);
                    used[i] = true;
                    dfs(candidates, result, path, used, target);
                    used[i] = false;
                    path.splice(path.length-1, 1);
                }
            } else {
                var flag = true;
                if(i>0) {
                    for(let j=0; j<i; j++) {
                        if(candidates[j] === candidates[i]) {
                            flag = false;
                        }
                    }
                } 
                if(flag) {
                    path.push(candidates[i]);
                    used[i] = true;
                    dfs(candidates, result, path, used, target);
                    used[i] = false;
                    path.splice(path.length-1, 1);
                }
            }
        }
    }
}

// 解法二: 仍然是没有在递归中全部去重，但递归中部分去重方法比上一个好，勉强提交成功，没有超时
var combinationSum2 = function(candidates, target) {
     var result = [];
    if(candidates.length === 0  || target === 0) {
        return;
    }
    candidates.sort((x, y) => {
        if(x < y) {
            return -1;
        } else if(x > y) {
            return 1;
        } else {
            return 0;
        }
    });

    var path = [];
    dfs(candidates, result, path, 0, target);

    var flaged = new Array(result.length);
    for(let i=0; i < flaged.length; i++) {
         flaged[i] = true;
    }

    for(let i=0; i< result.length-1; i++) {
         var string1 = result[i].join();
         for(let j=i+1; j<result.length; j++) {
            if(string1 === result[j].join()) {
                 flaged[i] = false;
            }
         }
    }
    var temp = [];
    for(let i = 0; i < flaged.length; i++) {
        if(flaged[i]) {
            temp.push(result[i]);
       }
    }

    return temp;
}

function dfs(candidates, result, path, start, target) {
    var sum = 0;
    for(let i = 0; i < path.length; i++) {
        sum = sum + path[i];
    }
    if(sum === target) {
        result.push(path.slice());
        return;
    } else if(sum > target) {
        return;
    }
    for(let i=start; i<candidates.length; i++) {
        path.push(candidates[i]);
        dfs(candidates, result, path, i+1, target);
        path.pop(candidates[i]);
    }
}



// 解法三: 真正的在递归中完整去重方法
var combinationSum2 = function(candidates, target) {
     var result = [];
    if(candidates.length === 0  || target === 0) {
        return;
    }
    candidates.sort((x, y) => {
        if(x < y) {
            return -1;
        } else if(x > y) {
            return 1;
        } else {
            return 0;
        }
    });

    var path = [];
    dfs(candidates, result, path, 0, target);
    return result;
}

function dfs(candidates, result, path, start, target) {
    var sum = 0;
    for(let i = 0; i < path.length; i++) {
        sum = sum + path[i];
    }
    if(sum === target) {
        result.push(path.slice());
        return;
    } else if(sum > target) {
        return;
    }
    for(let i=start; i<candidates.length; i++) {
        if(i > start && candidates[i-1] === candidates[i]) {
            continue;
        }
        path.push(candidates[i]);
        dfs(candidates, result, path, i+1, target);
        path.pop(candidates[i]);
    }
}
