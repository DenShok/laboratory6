num = []
s = 0
for i in range(10) :
    num.append(int(input()))
    if num[-1] > 5 :
        s += num[-1]
print(s)
