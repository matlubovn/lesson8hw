def func(lst: list):
    lst = list(set(lst))
    lst.sort()
    max2 = lst[-2]
    return max2

lst = [2,3,4,5,2,5,1,11,2,34,53,26,2]

print(func(lst))