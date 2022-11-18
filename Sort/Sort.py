from functools import wraps
import time

def sortTrace(func):                             # 호출할 함수를 매개변수로 받음
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("===============================================")
        start = time.time()  # 시작 시간 저장
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        print(f"before sort:    {args[0]}")
        value = func(*args, **kwargs)                               # 매개변수로 받은 함수를 호출
        print(f"after sort:     {value}")
        print(func.__name__, '함수 끝')
        print(f"실행시간: {time.time() - start:.10f} sec")
        return value
    return wrapper                           # wrapper 함수 반환

class Sort():
    @sortTrace
    def selectionSort(arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    @sortTrace
    def insertionSort(arr):
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break
        return arr


if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    Sort.selectionSort(array)
    Sort.insertionSort(array)