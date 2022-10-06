

N = int(input("введите количесво чисел: "))
a = []
for i in range(N):
    a.append(int(input()))
print("было: {0}".format(a))

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("стало: {0}".format(a))