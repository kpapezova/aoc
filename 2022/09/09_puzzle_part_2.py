# snake
# Count the number of position that the knot number 9 have visited at least once

visited_positions = []

with open("09_data.txt") as file:
    content = file.readlines()

S = [0, 0]      # S as start position, H and T at the same place. I have put start S in the middle of the field
knots =[[0, 0]] * 10    #0-9, 0 as head, 9 as the last knot


def move_head(head, direction):
    """Function that according the direction move the head"""
    if direction == "R":
        new_head = [head[0]+1, head[1]]
        return new_head
    elif direction == "L":
        new_head = [head[0]-1, head[1]]
        return new_head
    elif direction == "D":
        new_head = [head[0], head[1]-1]
        return new_head
    elif direction == "U":
        new_head = [head[0], head[1]+1]
        return new_head


def display(knots):
    """Display the movement of the head and the knots"""
    field_size = 20     # change if needed
    field = []

    for r in range(field_size, -field_size, -1):
        for c in range(-field_size, field_size):
            if c == 0 and r == 0:
                print("S", end=" ")
            elif [c, r] in knots:
                print(knots.index([c, r]), end=" ")
            else:
                print(".", end=" ")
            
            field.append(list((c, r)))
        print()
    #print(field)


def should_move_knot(head, knot):
    """Decide if the tail should move"""
    distance_x = head[0] - knot[0]
    distance_y = head[1] - knot[1]
    distance_x = abs(distance_x)
    distance_y = abs(distance_y)

    if distance_x > 1 or distance_y > 1 or distance_x+distance_y > 2:
        return True


def move_knot(knot_before, knot):
    """Move knot according the position of head and knot before"""
    distance_x = knot_before[0] - knot[0]
    distance_y = knot_before[1] - knot[1]

    knot_x = knot[0]
    knot_y = knot[1]

    if distance_x > 0:
        knot_x += 1
    elif distance_x < 0:
        knot_x -= 1
    if distance_y > 0:
        knot_y += 1
    elif distance_y < 0:
        knot_y -= 1

    new_position = [knot_x, knot_y]
    return new_position 


for line in content: 
    direction, steps = line.strip().split()
    steps = int(steps)
    for _ in range(steps):
        knots[0] = move_head(knots[0], direction)
        # print(display(knots))
        for i in range(1, 10):
            if should_move_knot(knots[i-1], knots[i]):
                knots[i] = move_knot(knots[i-1], knots[i])
                #print(display(knots))
            if knots[-1] not in visited_positions:
                visited_positions.append(knots[-1])
    # print(visited_positions)

print(len(visited_positions))