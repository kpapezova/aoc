# snake
# H as head
# T as tail
# the head (H) and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching)
# if H and T don´t touch, the tail must move
# 
# Count the number of position that the tail visited at least once


visited_positions = []

with open("09_data.txt") as file:
    content = file.readlines()

S = [0, 0]      # S as start position, H and T at the same place. I have put start S in the middle of the field
H = [0, 0]
T = [0, 0]

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


def display(head, tail):
    """Display the movement of the head"""
    field_size = 20     # change if needed
    field = []

    for r in range(field_size, -field_size, -1):
        for c in range(-field_size, field_size):
            if c == 0 and r == 0:
                print("S", end=" ")
            elif c == head[0] and r == head[1]:
                print("H", end=" ")
            elif c == tail[0] and r == tail[1]:
                print("T", end=" ")
            else:
                print(".", end=" ")
            field.append(list((c, r)))
        print()
    #print(field)


def should_move_tail(head, tail):
    """Decide if the tail should move"""
    distance_x = head[0] - tail[0]
    distance_y = head[1] - tail[1]
    distance_x = abs(distance_x)
    distance_y = abs(distance_y)

    if distance_x > 1 or distance_y > 1 or distance_x+distance_y > 2:
        return True


def move_tail(head, tail, direction):
    """Move tail according the position of head"""
    distance_x = head[0] - tail[0]
    distance_y = head[1] - tail[1]

    tail_x = tail[0]
    tail_y = tail[1]

    if distance_x > 0:
        tail_x += 1
    elif distance_x < 0:
        tail_x -= 1
    if distance_y > 0:
        tail_y += 1
    elif distance_y < 0:
        tail_y -= 1

    new_tail = [tail_x, tail_y]
    return new_tail 

for line in content: 
    direction, steps = line.strip().split()
    steps = int(steps)
    #print(type(direction), type(steps))
    for _ in range(steps):
        H = move_head(H, direction)
        #print(H)
        
        if should_move_tail(H, T) == True:
            T = move_tail(H, T, direction)
            if T not in visited_positions:
                visited_positions.append(T)

        #print(display(H, T))
    #print(visited_positions)

print(len(visited_positions))



