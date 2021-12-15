def nums_gen(n):
    generator = (num for num in range(1, n+1, 2))
    return generator

gen_5 = nums_gen(5)
for i in gen_5:
    print(i)