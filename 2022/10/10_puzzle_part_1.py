# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?

cycle_of_interesed = [20, 60, 100, 140, 180, 220]
cycles = 1

with open("10_test_data.txt") as file:
    input = file.readlines()


for line in input:
    line = line.strip()
    print(line)
    cycles += 1
    if "addx" in line:
        addx, value = line.split(" ")
        value = int(value)
        print("toto je hodnota", value)
    
print(cycles)