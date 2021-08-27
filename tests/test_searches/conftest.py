every_second = [i for i in range(0, 3000, 2)]
every_third = [i for i in range(0, 3000, 3)]
every_fifth = [i for i in range(0, 3000, 5)]
empty_list = []
random_list = [12, 108, 167, 314, 417, 490, 547, 547, 549, 1060, 1081, 1140, 1343, 1429, 1518, 1522, 1599, 1615, 1795, 1868, 1924]

test_cases_exist = [
    (every_second, 78, True),
    (every_second, 1997, False),
    (every_second, 0, True),
    (every_second, 3000, False),
    (every_third, 99, True),
    (every_third, 200, False),
    (every_third, 0, True),
    (every_third, 3000, False),
    (every_fifth, 455, True),
    (every_fifth, 139, False),
    (every_fifth, 0, True),
    (every_fifth, 3000, False),
    (every_fifth, -275, False),
    (empty_list, 15, False),
    (random_list, 547, True),
    (random_list, 1567, False),
    (random_list, 100000, False),
]

test_cases_idx = [
    (every_second, 78, 39),
    (every_second, 1997, -1),
    (every_second, 0, 0),
    (every_second, 3000, -1),
    (every_third, 99, 33),
    (every_third, 200, -1),
    (every_third, 0, 0),
    (every_third, 3000, -1),
    (every_fifth, 455, 91),
    (every_fifth, 139, -1),
    (every_fifth, 0, 0),
    (every_fifth, 3000, -1),
    (every_fifth, -275, -1),
    (empty_list, 15, -1),
    (random_list, 549, 8),
    (random_list, 1567, -1),
    (random_list, 100000, -1),
]
