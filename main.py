import random

border = []
values = [2, 4]

for row in range(4):
    for col in range(4):
        border.append(random.choice(values))
    print()


for i in range(4):
    for j in range(4):
        print(border[j], end=" ")
    print()
