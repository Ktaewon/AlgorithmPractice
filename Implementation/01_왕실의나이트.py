import sys

input = sys.stdin.readline

direction = (
    (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)
)
start = input()
x = ord(start[0]) - 97
y = int(start[1])

count = 0
print(x, y)

for d in direction:
    tx = x + d[0]
    ty = y + d[1]
    if tx < 1 or ty < 1 or tx > 8 or ty > 8:
        continue
    count += 1

print(count)