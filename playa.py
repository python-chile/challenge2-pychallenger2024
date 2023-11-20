from utils import select_food, get_burning_calories, get_calories

def test(n, f, tests, type_=None):
    success = failed = 0
    for inputs_, output_ in tests:
        try:
            if type_ == 'img':
                assert sum(r+g+b+a for r,g,b,a in ImageChops.difference(f(*inputs_), Image.open(output_)).getdata()) < 10
            else:
                print(n, f(*inputs_))
                assert f(*inputs_) == output_
            success += 1
        except AssertionError:
            failed += 1
    print(f"TEST {n}: {success} exitosos y {failed} erróneos")

tests1 = [
    (([('Sandía', 1000), ('Helado', 100), ('Cuchuflí', 30), ('Palmera', 10)], 300), {'consumed_energy': 300, 'consumed_food': [0, 1]}),
    (([('Sandía', 1000), ('Helado', 100), ('Cuchuflí', 30), ('Palmera', 10), ('Sandía', 1000), ('Helado', 100), ('Cuchuflí', 30), ('Palmera', 10)], 1000), {'consumed_energy': 690, 'consumed_food': [0, 1, 2, 4, 5]})

]
tests2 = [
    (([[0, 0, 0],[0, 0, 0], [0, 'B', 0]],), {'burning': 4, 'steps': 5}),
    (([[1, 1, 1],[1, 1, 1], [1, 'B', 1]],), {'burning': 4, 'steps': 5}),
    (([[2, 2, 2],[2, 2, 2], [2, 'B', 2]],), {'burning': 6, 'steps': 5}),
    (([[0, 100, 100],[100, 100, 0], ['B', 100, 100]],), {'burning': 4, 'steps': 7}),
    (([[1, 0, -1],[1, 0, -1], [1, 'B', -1]],), {'burning': 0, 'steps': 5})
]
tests3 = [
    (([('Sandía', 10), ('Helado', 1), ('Cuchuflí', 0.3), ('Palmera', 0.1)], [[0, 0, 0],[0, 0, 0], [0, 'B', 0]]), {'net_energy': 0.1, 'burning_rate': 0.8, 'consumendfood': {'Sandía': 10, 'Helado': 1, 'Cuchuflí': 0.3}}),
    ]

test(1, select_food, tests1)
test(2, get_burning_calories, tests2)
test(3, get_calories, tests3)
