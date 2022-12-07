arr = [4, 1, 8, 6, 2, 12, 3, 7]
n = len(arr)


def bubble():
    swap = False
    for i in range(0, n - 1):
        for j in range(0, (n - i - 1)):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            # end if
        # next j
    # next i
    return arr


print(bubble())
