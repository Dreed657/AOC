f = open("advent/day2/input", "r")
lines = f.read().splitlines()

maxByColor = {"red": 12, "green": 13, "blue": 14}

total = 0

for line in lines:
    found = {"red": 0, "green": 0, "blue": 0}

    [game, cubes] = line.split(": ")

    id = game.split(" ")[1]
    cubesInHand = cubes.split("; ")

    for c in cubesInHand:
        hand = c.split(", ")
        for h in hand:
            [count, color] = h.split(" ")
            if found[color] < int(count):
                found[color] = int(count)

    power = found["red"] * found["green"] * found["blue"]
    total += power
    # print(found, "power:", power)

print(total)
