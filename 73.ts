/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    const R: Set<number> = new Set();
    const C: Set<number> = new Set();

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            if (matrix[i][j] == 0) {
                R.add(i);
                C.add(j);
            }
        }
    }

    for (const i of R) {
        for (let j = 0; j < matrix[0].length; j++) {
            matrix[i][j] = 0;
        }
    }

    for (const i of C) {
        for (let j = 0; j < matrix.length; j++) {
            matrix[j][i] = 0;
        }
    }
}

setZeroes([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]);
