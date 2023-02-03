# You count the pixels on the CRT: 40 wide and 6 high.
# cycles // 40 -> to know what row
# cycles % 40 -> to know what column
# the sprite is 3 pixels wide, and the X register sets the horizontal position of the middle of that sprite. (x-1, x, x+1)

cycles = 0
register_X = 1
crt = [[],[],[],[],[],[]]       # 6 rows
#crt = [[] for x in range(6)]       # another approach to make a list of list (6 rows) 

with open("10_data.txt") as file:
    input = file.readlines()

def draw_pixel(cycle, x, crt):
    """From count of cycles the function evaluate the column and accordig the register_X decide what pixel to draw ("#" or ".")"""
    column = cycle % 40
    if column in (x-1, x, x+1):
        crt[cycle//40].append("#")
    else:
        crt[cycle//40].append(".")
    return crt


for line in input:
    line = line.strip()
    if cycles % 40 == 0:
        crt.append([])
    crt = draw_pixel(cycles, register_X, crt)
    cycles += 1

    if "addx" in line:
        addx, value = line.split(" ")
        value = int(value)
        crt = draw_pixel(cycles, register_X, crt)
        cycles += 1
        register_X += value

#Result
for row in crt:
    print("".join(row))