from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
arr = [False for _ in range(m)]


def tracking(k, before):
    global n, m, arr, visited
    if k == m:
        print(*arr, sep=" ")
        return
    for i in range(before + 1, n + 1):
        arr[k] = i
        tracking(k + 1, i)


tracking(0, 0)
