def binarySearchRecursion(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    # 중간점보다 작은 경우
    elif arr[mid] < target:
        return binarySearchRecursion(arr, target, start, mid - 1)
    # 중간점보다 큰 경우
    else:
        return binarySearchRecursion(arr, target, mid + 1, end)

def binarySearchIterative(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        # 중간점보다 작은 경우
        elif arr[mid] < target:
            end = mid - 1
        # 중간점보다 큰 경우
        else:
            start = mid + 1
    return None