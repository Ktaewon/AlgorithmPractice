from functools import wraps
import time

def sortTrace(func):                             # 호출할 함수를 매개변수로 받음
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("===============================================")
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        print(f"before sort:    {args[1]}")
        start = time.perf_counter()  # 시작 시간 저장
        value = func(*args, **kwargs)                               # 매개변수로 받은 함수를 호출
        end = time.perf_counter()
        print(f"after sort:     {value}")
        print(func.__name__, '함수 끝')
        print(f"실행시간: {(end - start) * 1000}ms")
        return value
    return wrapper                           # wrapper 함수 반환

class Sort():
    @sortTrace
    def selectionSort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    @sortTrace
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break
        return arr
    @sortTrace
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[0]
        tail = arr[1:]
        
        left_side = [x for x in tail if x <= pivot]
        right_side = [x for x in tail if x > pivot]
        
        return self.quickSort(left_side) + [pivot] + self.quickSort(right_side)
    @sortTrace   
    def countSort(self, arr):
        sorted_arr = []
        count = [0] * (max(arr) + 1)
        for i in range(len(arr)):
            count[arr[i]] += 1
        for i in range(len(count)):
            for j in range(count[i]):
                sorted_arr.append(i)
        return sorted_arr
    
if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    sort = Sort()
    sort.selectionSort(array)
    sort.insertionSort(array)
    #sort.quickSort(array)
    sort.countSort(array)