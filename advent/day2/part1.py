f = open("advent/day2/input", "r")
lines = f.read().splitlines()

maxByColor = {"red": 12, "green": 13, "blue": 14}

total = 0

for line in lines:
    [game, cubes] = line.split(": ")

    id = game.split(" ")[1]
    cubesInHand = cubes.split("; ")

    isPossible = True

    for c in cubesInHand:
        hand = c.split(", ")
        if not isPossible:
            break

        for h in hand:
            [count, color] = h.split(" ")

            if int(count) > maxByColor[color]:
                isPossible = False
                break
            else:
                isPossible = True

    if isPossible:
        total += int(id)

print(total)
