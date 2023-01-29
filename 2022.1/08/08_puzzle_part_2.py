# New Year brings new chalenges so let´s start to code in English :)

from pathlib import Path

here = Path(__file__).parent

trees = []

with open(here / "08_data.txt") as file:
    for line in file:
        trees.append(list(map(int, line.strip())))

total_count = 0

for r in range(1, len(trees)-1):     # r as row
    for c in range(1, len(line)-1):      # c as column
        coordinates = (r, c)
        #print(coordinates) 
        #print(trees[r][c])
        
        count_down = 0
        count_left = 0
        count_right = 0
        count_up = 0
        height = trees[r][c]        # height of examined tree
        print("vyska", height, "souradnice", r, c)

        for x in range(r+1, len(trees)):
            if trees[x][c] < height:
                count_down += 1
            else:
                count_down += 1
                break

        for x in range(r-1, -1, -1):
            if trees[x][c] < height:
                count_up += 1
            else:
                count_up += 1
                break

        for y in range(c+1, len(line)):
            if trees[r][y] < height:
                count_right +=1
            else:
                count_right += 1
                break

        for y in range(c-1, -1, -1):
            if trees[r][y] < height:
                count_left += 1
            else:
                count_left += 1
                break

        count = count_down * count_up * count_left * count_right

        if count > total_count:
            total_count = count

print(f"Best score: {total_count}")
