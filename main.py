import random

border = []
new_border = []
values = [2, 4]


def create_emp_border(some_border):
    for row in range(4):
        for col in range(4):
            some_border.append("-")
    return some_border


def create_random_border(some_border):
    for row in range(4):
        for col in range(4):
            some_border.append(random.choice(values))
        print()
    return some_border


def print_border(some_border):
    for row in range(4):
        for col in range(4):
            print(some_border[col], end=" ")
        print()


def start_move(some_border):
    first_point_x = random.randint(1, 2)
    first_point_y = random.randint(1, 2)

    second_point_x = random.randint(1, 2)
    second_point_y = random.randint(1, 2)

    some_border = some_border[:first_point_x][:first_point_y] + random.choice(values) + some_border[first_point_x][first_point_y]
    some_border = some_border[:second_point_x][:second_point_y] + random.choice(values) + some_border[second_point_x][second_point_y]

    return some_border


create_emp_border(border)
start_move(border)
print_border(border)
