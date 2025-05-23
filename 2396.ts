function convBaseN(n: number, b: number, m: number = 1) {
  if (n <= b) {
    return m * b;
  }

  return convBaseN(n / b, b, m * 10) + m * (n % b);
}

function isPalindromic(n: string): boolean {
  for (let i = 0; i < n.length / 2; i++) {
    if (n[i] !== n[n.length - 1 - i]) {
      return false;
    }
  }

  return true;
}

function isStrictlyPalindromic(n: number): boolean {
  for (let i = 2; i <= n - 2; i++) {
    let s = convBaseN(n, i).toString();

    if (!isPalindromic(s)) {
      return false;
    }
  }

  return true;
}
