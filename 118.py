# pyright: strict


def generate_pascal_triangle(n: int) -> list[list[int]]:
    pascal: list[list[int]] = []

    for i in range(0, n + 1):
        l: list[int] = []

        for j in range(i):
            if j == 0 or j == i - 1:
                l.append(1)
                continue

            l.append(pascal[i - 1][j - 1] + pascal[i - 1][j])

        pascal.append(l)

    pascal.pop(0)

    return pascal


print(generate_pascal_triangle(30))
