import sys

inputData = sys.stdin.readline().strip()

operand = []
operator = []

temp = ""
for ch in inputData:
    if ord(ch) >= 48 and ord(ch) <= 57:
        temp += ch
    else:
        operator.append(ch)
        operand.append(int(temp))
        temp = ""
operand.append(int(temp))
result = operand.pop(0)
tempsum = 0
flag = 0
while(len(operand) != 0):
    opt = operator.pop(0)
    if opt == '-':
        if flag == 1:
            result -= tempsum
            tempsum = 0
        flag = 1
        tempsum += operand.pop(0)
    else:
        if flag == 0:
            result += operand.pop(0)
        else:
            tempsum += operand.pop(0)
result -= tempsum
print(result)
