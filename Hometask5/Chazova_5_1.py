def nums_gen(n):
    for num in range(1, n+1, 2):
        yield num


nums_gen_15 = nums_gen(15)
print(next(nums_gen_15))
print(next(nums_gen_15))