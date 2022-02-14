s = ''
with open('dataset_3363_2.txt', 'r') as f:
    a = f.readline().strip()
    for i in range(len(a)):
        if a[i] > "A":
            s += f' {a[i]} '
        else:
            s += a[i]
b = s.split()
for j in range(len(b)):
    if b[j] > "A":
        print(b[j], end='')
    elif b[j] < "A":
        print(b[j - 1] * (int(b[j]) - 1), end='')












