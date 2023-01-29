# New Year brings new chalenges so let´s start to code in English :)

from pathlib import Path

here = Path(__file__).parent

trees = []

with open(here / "08_data.txt") as file:
    for line in file:
        trees.append(list(map(int, line.strip())))

count_visible_trees = 0

for r in range(1, len(trees)-1):     # r as row
    for c in range(1, len(line)-1):      # c as column
        coordinates = (r, c)
        #print(coordinates) 
        #print(trees[r][c])

        height = trees[r][c]        # height of examined tree
        for x in range(r+1, len(trees)):
            if height <= trees[x][c]:
                break
        else:
            count_visible_trees += 1
            continue

        for x in range(r-1, -1, -1):
            if height <= trees[x][c]:
                break
        else:
            count_visible_trees += 1
            continue

        for y in range(c+1, len(line)):
            if height <= trees[r][y]:
                break
        else:
            count_visible_trees += 1
            continue

        for y in range(c-1, -1, -1):
            if height <= trees[r][y]:
                break
        else:
            count_visible_trees += 1
            continue

count_visible_trees += len(trees)*2 + len(line)*2 -4
print(f"number of visible trees: {count_visible_trees}")
