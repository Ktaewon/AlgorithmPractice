import random
import string

def checkMissedRequirements(password, n):
    re_ch = False
    re_up = False
    re_lo = False
    re_di = False
    re_sp = False
    if n < 7:
        re_ch = False
    else:
        re_ch = True
    for ch in password:
        # 문자라면,
        if ch.isalpha():
            # 대문자 있는지
            if not re_up and ch.isupper():
                re_up = True
            # 소문자 있는지
            if not re_lo and ch.islower():
                re_lo = True
        # 숫자 있는지
        elif not re_di and ch.isdigit():
            re_di = True
        # 특수문자(#, @, *, &) 있는지
        elif not re_sp and (ch == '#' or ch == '@' or ch == '*' or ch == '&'):
            re_sp = True
        if re_ch and re_up and re_lo and re_di and re_sp:
            break
    return ([re_ch, n], re_up, re_lo, re_di, re_sp)

def correctPass(password, re_miss_lists):
    if re_miss_lists[1] == False:
        password += random.choice(string.ascii_letters).upper()
        re_miss_lists[0][1] += 1
    if re_miss_lists[2] == False:
        password += random.choice(string.ascii_letters).lower()
        re_miss_lists[0][1] += 1
    if re_miss_lists[3] == False:
        password += str(random.randint(0, 9))
        re_miss_lists[0][1] += 1
    if re_miss_lists[4] == False:
        password += random.choice(['#', '@', '*', '&'])
        re_miss_lists[0][1] += 1
    if re_miss_lists[0][0] == False:
        for i in range(max(7 - re_miss_lists[0][1], 0)):
            password += random.choice(string.ascii_letters)
    return password

def checkAndCorrectPass(password, n):
    re_miss_lists = checkMissedRequirements(password, n)
    new_password = correctPass(password, re_miss_lists)
    return new_password

# T : the number of test cases
T = int(input())
answers = []

for i in range(T):
    # N : the length of the old password.
    # Old password contains only digits, 
    # letters, and special characters.
    N = int(input())
    old_pw = input()
    answers.append(checkAndCorrectPass(old_pw, N))
for i in range(T):
    print("Case #{}: {}".format(i + 1, answers[i]))