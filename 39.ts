function combinationSum(candidates: number[], target: number): number[][] {
    let res: number[][] = [];

    candidates.sort();

    for (let i = 0; i < candidates.length; i++) {
        let n = candidates[i];
        let c = n;
        let m = 1;

        if (n == target) {
            res.push([c]);
        }

        while (c <= target) {
            // console.log(c);

            // if (target - c == n) {
            //     res.push(Array(m).fill(n + 1));
            // }

            let arr: number[] = [];
            let f = candidates.indexOf(target - c);
            console.log(c, target - c, f);

            if (f != -1 && (f >= i || m > 1)) {
                for (let i = 0; i < m; i++) {
                    arr.push(n);
                }

                arr.push(candidates[f]);
            }

            if (arr.length != 0) {
                res.push(arr);
            }

            m++;
            c += n;
        }
    }

    console.log(res);

    return res;
}

// combinationSum([2, 3, 6, 7], 7);
// combinationSum([2, 3, 5], 8);

combinationSum([7, 3, 2], 18);
