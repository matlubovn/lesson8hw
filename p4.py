def func(lst: list):
    max_count = lst.count(lst[0])
    max_value = lst[0]
    for i in lst:
        new_count = lst.count(i)
        if new_count > max_count:
            max_count = new_count
            max_value = i
    return max_value, max_count


lst = [5,1,7,4,5,7,4,7,3,7,5,7,2,7,3,7,5,5,7,0,7]

print(func(lst))
