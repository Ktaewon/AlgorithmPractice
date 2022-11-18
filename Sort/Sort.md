# Sort Algorithm(정렬 알고리즘)
## 알고리즘 정리
* 정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것.
## 알고리즘 종류
### 1. Bubble Sort(거품 정렬)
* 인접한 두 원소의 대소를 비교하고, 조건에 맞지 않다면 자리를 교환하여 정렬하는 알고리즘
* 방법
    1. 1회전을 수행하면서, 1번째와 2번째, 2번째와 3번째, 이렇게 마지막 - 1 번째와 마지막을 비교해가며 조건에 맞지 않다면 교환한다.
    2. 1회전이 끝나면, 가장 큰 원소가 제일 뒤로 이동하게 된다. 2회전을 수행할 때는 제일 마지막 원소는 제외되고, 그 중 가장 큰 원소가 끝에서 2번째에 위치하게 된다. 이렇게 회전을 계속 수행하며 정렬해 나가게 된다.
* 이해가 쉬운 이미지
    * <img src="https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/bubble-sort-001.gif"></img>
    * 출처: https://github.com/GimunLee/tech-refrigerator/blob/master/Algorithm/resources/bubble-sort-001.gif
* 공간 복잡도: **O(n)**
* 시간 복잡도: **O(n<sup>2</sup>)**
    * Best: O(n<sup>2</sup>)
    * Avg:  O(n<sup>2</sup>)
    * Worst: O(n<sup>2</sup>)
- Stable
- in-place
### 2. Selection Sort(선택 정렬)
* 가장 작은 것을 선택해 맨 앞의 데이터와 바꾸는 것을 반복하는 알고리즘
    * 순환하면서 최소 or 최대 값을 찾아 현재 원소 위치와 교환하는 방식
* 공간 복잡도: **O(n)**
* 시간 복잡도: **O(n<sup>2</sup>)**
- Unstable
- In-place
### 3. Insertion Sort(삽입 정렬)
* 데이터를 특정한 위치에 삽입한다는 의미에서 "삽입 정렬"이라고 한다
* 2번째 원소부터 시작하여 그 앞(왼쪽)의 원소들과 비교하여 삽입할 위치를 지정한 후, 원소를 뒤로 옮기고 지정된 자리에 자료를 삽입한다
* 공간 복잡도: **O(n)**
* 시간 복잡도: **O(n<sup>2</sup>)**
    * Best: **O(n)*
        - 이미 정렬되어 있는 경우 O(n)의 시간을 가진다.
    * Avg:  O(n<sup>2</sup>)
    * Worst: O(n<sup>2</sup>)
- Stable
- In-place
- 이미 어느정도 정렬되어 있는 경우, 매우 효율적
### 4. Quick Sort
### 5. Merge Sort
### 6. Heap Sort
### 7. Radix Sort
### 8. Counting Sort
