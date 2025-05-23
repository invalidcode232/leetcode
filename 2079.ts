function wateringPlants(plants: number[], capacity: number): number {
  let m = plants[0];
  let n = 1;
  let i = 0;
  let rem = capacity;

  while (i < plants.length) {
    m = plants[i];
    rem -= m;
    // console.log(m, n);

    if (rem >= 0) {
      n++;
    } else {
      // console.log("ss");
      n += 2 * i + 1;
      rem = capacity;
      rem -= m;
    }

    i++;
  }

  return n - 1;
}

console.log(wateringPlants([7, 7, 7, 7, 7, 7, 7], 8));
