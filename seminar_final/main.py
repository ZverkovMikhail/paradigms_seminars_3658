def binary_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def print_result(res, n):
    if res != -1:
        print('%d is present at index => %d' % (n, res))
    else:
        print('Array is not contains %d' % n)


if __name__ == '__main__':
    array = [1, 2, 6, 8, 31, 56, 87, 90]
    num = 3
    num2 = 87
    print_result(binary_search(array, 0, len(array) - 1, num), num)
    print_result(binary_search(array, 0, len(array) - 1, num2), num2)


