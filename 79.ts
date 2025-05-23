function exist(board: string[][], word: string): boolean {
  let ans = false;

  let im = board.length;
  let jm = board[0].length;

  function exist_iter(i: number, j: number, k: number) {
    if (i < 0 || i >= im || j < 0 || j >= jm) {
      return;
    }

    if (board[i][j] == "*") {
      return;
    }

    if (k == word.length - 1 && board[i][j] == word[k]) {
      ans = true;
      return;
    }

    if (board[i][j] != word[k]) {
      return;
    }

    let prev = board[i][j];
    board[i][j] = "*";

    exist_iter(i + 1, j, k + 1);
    exist_iter(i - 1, j, k + 1);
    exist_iter(i, j + 1, k + 1);
    exist_iter(i, j - 1, k + 1);
    board[i][j] = prev;
  }

  for (let i = 0; i < im; i++) {
    for (let j = 0; j < jm; j++) {
      exist_iter(i, j, 0);
    }
  }

  return ans;
}
