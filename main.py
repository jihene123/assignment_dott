import numpy as np

def solve(arr, n, m):
    mem = np.full((n, m), -1)
    mem2 = np.full((n, m), -1)
    mem3 = np.full((n, m), -1)
    mem4 = np.full((n, m), -1)

    def fill(x, y, dx, dy, mem):
        if x >= n or y >= m or x < 0 or y < 0:
            return 999999
        if mem[x][y] != -1:
            return mem[x][y]
        if arr[x][y] == 1:
            mem[x][y] = 0
            fill(x+dx, y, dx, dy, mem)
            fill(x, y+dy, dx, dy, mem)
            return 0

        mem[x][y] = 1 + min(fill(x+dx, y, dx, dy, mem), fill(x, y+dy, dx, dy, mem))
        return mem[x][y]

    fill(0, 0, 1, 1, mem)
    fill(0, m-1, 1, -1, mem2)
    fill(n-1, 0, -1, 1, mem3)
    fill(n-1, m-1, -1, -1, mem4)

    for i in range(n):
        for j in range(m):
            mem[i][j] = min(mem[i][j], mem2[i][j])
            mem[i][j] = min(mem[i][j], mem3[i][j])
            mem[i][j] = min(mem[i][j], mem4[i][j])
    return mem


if __name__ == "__main__":
    T = input()
    for t in range(int(T)):
        n, m = input().split()
        array = np.zeros((int(n), int(m)))
        for i in range(int(n)):
            array[i, :] = [c for c in input()]
        result = solve(array, int(n), int(m))
        for i in range(int(n)):
            for j in range(int(m)):
                print(result[i][j], ' ', end='')
            print('')
        if t < int(T) - 1:
            input()