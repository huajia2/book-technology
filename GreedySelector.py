s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
k = []
a = 0


def GreedySelector(n, s, f):
    print("\n\n当s[i-1]>f[j-1]时i才会赋给j\n\n")
    print("s[i-1]----f[j-1]----------  i   j")
    i = j = 1  # 作为贪心选择的开始点,从这开始，故这里也算
    print(s[i - 1], "---------", f[j - 1], "------------ [", i, " ", j, "]-----------", j)
    k.append(j)

    for i in range(2, n + 1):
        if (s[i - 1] > f[j - 1]):
            j = i
            print(s[i - 1], "---------", f[j - 1], "------------[", i, " ", j, "]-----------", j)
            k.append(j)
        else:
            print(s[i - 1], "---------", f[j - 1], "------------ ", i, " ", j)

    return k


GreedySelector(11, s, f)

print("\n\t\t\t活动时间图\n")
for l in range(len(k)):
    if (a == 0):
        print("\t活动", k[l], "\n     ┗", end="")
        print("━" * (f[k[l] - 1] - s[k[l] - 1]), end="┛\n")
        print("     ", s[k[l] - 1], ((f[k[l] - 1] - s[k[l] - 1]) + 1) * " ", f[k[l] - 1], end="\n")
        a = a + f[k[l] - 1]
    else:
        a = a + f[k[l] - 1]
        print((a + (f[k[l] - 1] - s[k[l] - 1])) * " ", " 活动", k[l], "\n")
        print((a + (f[k[l] - 1] - s[k[l] - 1])) * " ", "┗", end="")
        print("━" * (f[k[l] - 1] - s[k[l] - 1]), end="┛\n")
        print((a + (f[k[l] - 1] - s[k[l] - 1])) * " ", s[k[l] - 1], ((f[k[l] - 1] - s[k[l] - 1]) + 1) * " ",
              f[k[l] - 1], end="\n")

print("\n        活动序号：", end="   ")
for l in range(len(k)):
    print("[", end="")
    print(k[l], end="]  ")
print("\n该活动起始时间si：", end="    ")
for m in range(len(k)):
    print(s[k[m] - 1], end="    ")
print("\n该活动结束时间fi：", end="    ")
for n in range(len(k)):
    print(f[k[n] - 1], end="    ")