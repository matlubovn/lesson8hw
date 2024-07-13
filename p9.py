def func(dct: dict):
    new_dct = {}
    for key, value in dct.items():
        new_dct[value] = key
    return new_dct


dct = {

    'data': 100,
    'info': 120,
    'smth': 222,
    'bmw': '150',

}

print(func(dct))