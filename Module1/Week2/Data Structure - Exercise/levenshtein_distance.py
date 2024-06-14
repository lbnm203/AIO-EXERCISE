def levenshtein_distance(source, target):
    m = len(source)
    n = len(target)

    D = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        D[i][0] = i

    for j in range(n + 1):
        D[0][j] = j

    print('Ma trận trước khi fill: ')
    for i in range(m + 1):
        for j in range(n + 1):
            print(D[i][j], end=" ")
        print()

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                del_cost = D[i - 1][j]
                ins_cost = D[i][j - 1]
                sub_cost = D[i - 1][j - 1]
                D[i][j] = min(del_cost, ins_cost, sub_cost) + 1

    print('Ma trận sau khi fill: ')
    for i in range(m + 1):
        for j in range(n + 1):
            print(D[i][j], end=" ")
        print()

    return D[m][n]


if __name__ == "__main__":
    source = input('')
    target = input('')

    distance = levenshtein_distance(source, target)
    print(f'Khoảng cách Levenshstein của {source} và {target} là: {distance}')
