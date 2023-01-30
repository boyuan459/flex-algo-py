
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = int((left + right) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    idx = binary_search(arr, 4)
    print(idx)
