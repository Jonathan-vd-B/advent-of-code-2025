def process_instructions() -> list[int]:
    instructions: list[int] = []

    with open("python/day1/rotations.txt") as file:
        for line in file:
            line = line.strip()
            
            if line[0] == "L":
                instructions.append(-int(line[1:]))
            else:
                instructions.append(int(line[1:]))

    print(instructions)
    return instructions

instructions: list[int] = process_instructions()
pos = 50  # starting position
zero_counter = 0

for rotation in instructions:
    full_rots = abs(rotation) // 100
    rotation = rotation - (full_rots * 100) if rotation > 0 else rotation + (full_rots * 100)
    zero_counter += full_rots
    
    new_pos = (pos + rotation) % 100

    if rotation < 0 and new_pos >= pos and new_pos != 0 and pos != 0:
        zero_counter += 1
    if rotation > 0 and new_pos <= pos and new_pos != 0 and pos != 0:
        zero_counter += 1

    pos = new_pos
    if pos == 0:
        zero_counter += 1
    print(pos)

print(f"Number of times position 0 was reached: {zero_counter}")
