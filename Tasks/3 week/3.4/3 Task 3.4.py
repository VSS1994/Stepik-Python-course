with open('dataset_3363_4.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    counter = 0
    personal_avg = 0
    math_avg = 0
    phys_avg = 0
    russ_avg = 0
    for i in lines:
        for j in i.split(';')[1 : ]:
            counter += 1
            personal_avg += int(j)
            if counter == 1:
                math_avg += int(j)
            elif counter == 2:
                phys_avg += int(j)
            elif counter == 3:
                russ_avg += int(j)
        print(personal_avg / 3)
        personal_avg = 0
        counter = 0
print(math_avg / len(lines), phys_avg / len(lines), russ_avg / len(lines))