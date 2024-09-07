import random
import math

r = int(input("Radius : "))
while True:
    coordinates = []
    while True:
        x = random.randint(-r, r)
        y = random.randint(-r, r)

        if x ** 2 + y ** 2 == r ** 2:
            coordinates.append([x, y])
        else:
            continue

        if len(coordinates) == 3:
            break

    def calculate_distance(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    d1 = calculate_distance(coordinates[0], coordinates[1])
    d2 = calculate_distance(coordinates[0], coordinates[2])
    d3 = calculate_distance(coordinates[1], coordinates[2])


    if d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1:
        print("Coordinates Denoting A Triangle : ", coordinates)
        break
    else:
        continue
