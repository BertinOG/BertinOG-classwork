arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
L = 1
R = len(arr)
M = (L + R) // 2

print(L, M, R)


def BinarySearch(target):
    global L, M, R
    if arr[M] == target:
        return M
    elif target < M:
        R = M - 1
        M = (L + R) // 2
        print(L, M, R)
        BinarySearch(target)
    elif target > M:
        L = M + 1
        M = (L + R) // 2
        print(L, M, R)
        BinarySearch(target)


BinarySearch(8)
