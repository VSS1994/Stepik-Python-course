s = ''
l = []
c = 0
with open('dataset_3363_3 (2).txt', 'r') as f:
    for i in f.readlines():
        s += i.lower()
    s = sorted(s.split())
    for i in s:
        if i not in l:
            cnt = s.count(i)
            if len(l) == 2:
                if cnt > l[1]:
                    l[0] = i
                    l[1] = cnt
            else:
                l.append(i)
                l.append(cnt)
                c = cnt
print(*l)

#альтернативный вариант
c = 0
with open('dataset_3363_3 (2).txt', 'r') as f:
    s = f.read().lower().strip().split()
    s = sorted(s)
    for i in s:
        cnt = s.count(i)
        if cnt > c:
            c = cnt
            w = i
print(w, c)










