import numpy as np

# More compact way of doing it (should learn this and make it standard):
mapping = {".": 0, "@": 1}

with open("python/day4/input.txt", "r") as file:
    rows: list[list[int]] = [[mapping[element] for element in line.strip()] for line in file]

grid = np.array(rows)

grid = np.pad(grid, pad_width=1, mode="constant", constant_values=0)  # pads around array value 0 to not have to deal with special border logic
print(grid)
print(grid[1,1], grid[10,1])  # indexing is 1 shifted now. Lefttop corner is not 0,0 anymore but 1,1


rolls_moved = 0
while True:
    rolls_moved_at_start = rolls_moved
    
    accessible_rolls = 0
    # iterate over each spot
    for row_idx in range(len(grid)):
        if row_idx != 0 and row_idx != len(grid) - 1:  # skip if in padding rows
            for column_idx in range(len(grid)):
                if column_idx != 0 and column_idx != len(grid) - 1:  # skip if in padding columns
                    if grid[row_idx, column_idx] == 1:  # paperroll
                        slicing = grid[row_idx-1 : row_idx+2, column_idx-1 : column_idx+2]  # +2 since last item of slicing is not included
                        print()
                        print(slicing)
                        print(f"Rowindex = {row_idx} and Columnindex = {column_idx}")
                        
                        adjacent_rolls = np.sum(slicing) - 1  # -1 to subtract roll itself
                        if adjacent_rolls < 4:
                            print(f"Adding a roll to accessibles! Total is now {accessible_rolls + 1}!")
                            accessible_rolls += 1
                            grid[row_idx, column_idx] = 0
                            print(slicing)

    print(f"Paper-rolls that can be accesed by a forklift sum to a total of {accessible_rolls}")
    rolls_moved += accessible_rolls

    rolls_moved_at_end = rolls_moved
    if rolls_moved_at_end == rolls_moved_at_start:  # this means we have not moved any rolls this iteration.
        break


print(f"\nWe moved a total of {rolls_moved} paper-rolls\n")

