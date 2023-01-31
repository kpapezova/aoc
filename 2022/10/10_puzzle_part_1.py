# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?

cycles = 0
register_X = 1
signals_strength = 0

with open("10_test_data.txt") as file:
    input = file.readlines()

def cycles_evaluation(cycle, value_X):
    """Function for evaluation of signal strength"""
    cycle_of_interesed = [20, 60, 100, 140, 180, 220]
    if cycle in cycle_of_interesed:
        return int(cycle * value_X)

    else:
        return 0


for line in input:
    line = line.strip()
    print(line)
    cycles += 1
    signals_strength += cycles_evaluation(cycles, register_X)
    print("signal strengt", signals_strength)
    
    if "addx" in line:
        addx, value = line.split(" ")
        value = int(value)
        cycles += 1
        register_X += value
        print("cyklus po addx", cycles, "value", value, "x", register_X)
        signals_strength += cycles_evaluation(cycles, register_X)
        print("signal strengt", signals_strength)

    # if cycles in cycle_of_interesed:
    #     print("cycles", cycles)
    #     print(cycle_of_interesed)
    #     print("X", register_X)
    #     signals_strength += (cycles*register_X)
    #     print("signals, strength", signals_strength)

print(signals_strength)