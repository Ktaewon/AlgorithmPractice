import sys

input = sys.stdin.readline

N = int(input())
move = list(input().split())

direction = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

x = 1
y = 1

for m in move:
    tx = x + direction[m][0]
    ty = y + direction[m][1]
    if tx < 1 or ty < 1 or tx > N or ty > N:
        continue
    x, y = tx, ty

print(x, y)