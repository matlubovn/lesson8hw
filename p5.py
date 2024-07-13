def func(lst: list):
    min_count = lst.count(lst[0])
    min_value = lst[0]
    for i in lst:
        new_count = lst.count(i)
        if new_count < min_count:
            min_count = new_count
            min_value = i
    return min_value, min_count


lst = [5,1,1,4,5,2,4,6,3,7,5,3,2,6,3,7,5,5,7,0]

print(func(lst))