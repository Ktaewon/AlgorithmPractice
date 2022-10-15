# 파이썬에서의 Stack(FILO)
# stack은 기존 List를 이용하여 구현할 수 있다
# 1. 선언
stack = []
# 2. 삽입
stack.append(3)
# 3. 삭제
stack.pop()


# 파이썬에서의 Queue(FIFO)
# queue는 deque를 이용해 구현할 수 있다
# deque는 스택과 큐의 장점을 모두 채택
# 데이터 넣고 빼는 속도가 리스트에 비해 빠르다
from collections import deque
# 1. 선언
queue = deque()
# 2. 삽입
queue.append(5)
# 3. 삭제
queue.popleft()
# 4. 리스트 변환
queue_list = list(queue)
