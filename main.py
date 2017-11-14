import random
import string
import copy

possible_words = []
m = [[random.choice(string.ascii_letters.upper()) for i in range(6)] for j in range(6)]

for r in m:
    print(r)


def traverse(tuple_xy, depth, carried_string, been_there):
    x = tuple_xy[0]
    y = tuple_xy[1]
    if depth > 5:
        return

    carried_string += m[x][y]

    been_there[x][y] = True
    possible_words.append(carried_string)

    depth += 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x = x + i
            new_y = y + j
            if new_x < 0 or new_x > 5 or new_y < 0 or new_y > 5:
                continue

            if not been_there[new_x][new_y]:
                traverse((new_x, new_y), depth, carried_string, copy.deepcopy(been_there))


for x in range(6):
    for y in range(6):
        print("I'm looking for x: "+str(x)+" y: "+str(y))
        traverse((x, y), 0, "", [[False for i in range(6)] for j in range(6)])

print(possible_words.__len__())
print(possible_words)
