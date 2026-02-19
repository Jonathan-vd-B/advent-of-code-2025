ranges: list[tuple[int, int]] = []  # A list of tuples consisting of start and end of fresh ranges.

available_ingredients: list[int] = []  # list of ingredients available in kitchen that are needed to be checked wether they are fresh.
fresh_ingredients: list[int] = []
spoiled_ingredients: list[int] = []

with open("python/day5/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        elements = line.split("-")

        if len(elements) == 2:
            ranges.append((int(elements[0]), int(elements[1])))
            # print(f"Adding range {elements}")
        elif len(elements) == 1:
            if elements[0] == "":
                print("\nWe are now switching to ingredients, coming from ranges\n")
            else:
                available_ingredients.append(int(elements[0]))
        else:
            print("\n\nTHIS SHOULD NOT BE PRINTED\n\n")

#GOTTEN FROM COPILOT
ranges.sort()
merged: list[tuple[int, int]] = []
for start, end in ranges:
    if merged and start <= merged[-1][1] + 1:  # overlapping or adjacent
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))
ranges = merged

print(ranges)

def tally(ranges: list[tuple[int, int]]) -> int:
    total = 0

    for range_ in ranges:
        range_length = range_[1] - range_[0] + 1
        total += range_length

    return total

print(tally(ranges))
    