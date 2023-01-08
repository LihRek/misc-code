info = dict()


def minimum():

    for student in info:
        min_score = 200
        min_pos = -1
        for num in range(len(info[student])):
            if info[student][num] == -1:
                continue
            if info[student][num] < min_score:
                min_score = info[student][num]
                min_pos = num
        print(student, min_pos, min_score)


def missing():
    for student in info:
        ans = list()
        for num in range(len(info[student])):
            if info[student][num] == -1:
                ans.append(num)
        if len(ans) == 0:
            print(student, "NONE")
        else:
            print(student, *ans)


n, m = input().split()
n = int(n)
m = int(m)
for i in range(m):
    name, number, score = input().split()
    number = int(number)
    score = int(score)
    try:
        info[name]
    except:
        info[name] = list()
        for j in range(n):
            info[name].append(-1)

    info[name][number] = score
action = input()
if action == "min":
    minimum()
else:
    if action == "missing":
        missing()