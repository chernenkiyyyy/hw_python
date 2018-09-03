

str_1 = [1, 2, [3, 4, [5, 6], 7], 8]

def my_gen(str):
    for i in str:
        if type(i) == int:
            yield i
        else:
            for j in i:
                if type(j) == int:
                    yield j
                else:
                     for n in j:
                         yield n

gen = my_gen(str_1)
for i in range(8):
    print(next(gen))




