# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?

cycle_of_interesed = [20, 60, 100, 140, 180, 220]
cycles = 0
register_X = 1
signals_strength = 0

with open("10_test_data.txt") as file:
    input = file.readlines()

# def cycles_evaluation(cycle, cycle_of_interesed, value_X):
#     """Function for evaluation of signal strength"""
#     if cycle in cycle_of_interesed:
#         return cycle * value_X



for line in input:
    line = line.strip()
    print(line)
    cycles += 1
    if "addx" in line:
        addx, value = line.split(" ")
        value = int(value)
        print("toto je hodnota", value)
        cycles += 1
        register_X += value

    if cycles in cycle_of_interesed:
        signals_strength += (cycles*register_X)

        # signals_strength += cycles_evaluation(cycles, cycle_of_interesed, register_X)

print(signals_strength)