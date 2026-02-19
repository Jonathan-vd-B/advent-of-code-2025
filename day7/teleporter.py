import numpy as np
import numpy.typing as npt

source_diagram: list[list[int]] = []

with open("python/day7/input.txt", "r") as f:
    for line in f:
        line = line.strip()
        row: list[int] = []
        for char in line:
            if char == ".":
                row.append(0)
            elif char == "^":
                row.append(-1)
            elif char == "S":
                row.append(1)
            else:
                print("This should not be printed")
                exit()
        source_diagram.append(row)

diagram: npt.NDArray[np.int_] = np.array(source_diagram)

# print(diagram)

for row in diagram:
    print(row)


splits = 0
timelines = 0
for r, row in enumerate(diagram):
    
    if r == len(diagram) - 1:  # reached last row, beams cannot be drawn on non-existing row.
        break

    for c, char in enumerate(row):
        if char > 0:
            if diagram[r + 1][c] != -1:  # cell directly below beam
                diagram[r + 1][c] += char
            else:
                diagram[r + 1][c - 1] += char
                diagram[r + 1][c + 1] += char
                splits += 1                


print(diagram)

print(f"\nA total number of {splits} splits were performed!")

timelines = sum(diagram[-1])

print(f"A total number of {timelines} timelines are created during the splitting process.")