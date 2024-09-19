list_ = []
for i in range(3, 21):
    first_number = i
    for j in range(1, first_number):
        second_number = j + 1
        for b in range(second_number, first_number):
            if first_number % (j + b) == 0:
                list_.append(j)
                list_.append(b)
    print(i, *list_)
    list_.clear()