three_d = [
                [
                    [1, 2, 3, 4],
                    [0, -1, -2, -3, -4, -5, -6]
                ],
                [
                    [1, 10, 15, 12, 20, 20, 20],
                    [-15, -13, 14, 20, -1]
                ]
        ]

flatten_list = []

for l3 in three_d:
    for l2 in l3:
        if len(l2) > 4:
            flatten_list.append(l2)

print(flatten_list)