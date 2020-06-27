/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
function dfs(n, k, result, path, depth, used) {
    if(depth === k) {
        // (10, 7)时超出时间限制
        // var repeated = result.some((list) => {
        //     var string = list.join();
        //     for(let i = 0; i < path.length; i++) {
        //         let temp = path[i].toString();
        //         if(string.indexOf(temp) === -1) {
        //             return false;
        //         }
        //     }
        //     return true;
        // });
        // if(!repeated) {
        //     result.push(path.slice());
        // }

        result.push(path.slice());
    }

    for(let i = 0; i < n; i++) {
        if(!used[i]) {
            if(path[path.length - 1]) {
                if(path[path.length - 1] < (i+1)) {
                    path.push(i+1);
                    used[i] = true;
                    dfs(n, k, result, path, depth+1, used);
                    used[i] = false;
                    path.splice(path.length-1, 1);
                }
            } else {
                path.push(i+1);
                used[i] = true;
                dfs(n, k, result, path, depth+1, used);
                used[i] = false;
                path.splice(path.length-1, 1);
            }   
        }
    }
}

var combine = function(n, k) {
    var result = [];
    var path = [];
    if(n === k) {
        for(let i = 1; i <= n; i++) {
            path.push(i);
        }
        result.push(path);
        return result;
    }
    if(n <= 0 || k <= 0) {
        return;
    }

    var used = new Array(n);
    for(let i = 0; i < used.length; i++) {
        used[i] = false;
    }
    
    dfs(n, k, result, path, 0, used);
    return result;
};
