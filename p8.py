def func(dct: dict):
    lst = []
    for key, value in dct.items():
        lst.append(key)
        lst.append(value)
    return lst


dct = {

    'data': 100,
    'info': 120,
    'smth': 222,
    'bmw': '150',

}

print(func(dct))