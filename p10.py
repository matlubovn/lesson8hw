def func(dct: dict, key):
    if key in dct:
        del dct[key]
    return dct


dct = {'a': 1, 'b': 2, 'c': 3}
minus = 'b'
print(func(dct, minus))