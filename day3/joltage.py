lines: list[list[int]] = []

with open("python/day3/input.txt", "r") as f:
    for line in f:
        line = line.strip()
        numbers: list[int] = []
        for number in line:
            numbers.append(int(number))
        lines.append(numbers)

# print(lines)

def is_valid_placement(spot_in_bank: int, digit: int, length: int):
    """
    Checks wether a change at the current spot in the battery bank is possible.
    It is only possible if all upcoming batteries can still be placed.

    batterybank is our 12 batteries
    sample is the chunk of batteries provided from which we have to choose 12.
    """
    battery_bank_length = 12
    
    sample_spot = digit
    remaining_bank_length = battery_bank_length - spot_in_bank - 1  # e.g. length 12, spot 0 = 11 -> 11 digits need to be able to be placed after this one
    sample_length = length

    if sample_spot + remaining_bank_length < sample_length:  # e.g. sample_spot 10, remaining_bank_lenght 4 < 15
        return True
    else:
        return False

def fill_remainder_with_zeros(battery_bank: list[int], battery: int):
    """
    Fill remainder of bank with zeros to be filled later
    """

    for i in range(len(battery_bank)):
        if i > battery:
            battery_bank[i] = 0

    return battery_bank


joltages: list[int] = []

for line in lines:  # finding joltage in each battery bank
    battery_bank: list[int] = []  # battery_bank of 12 batteries
    for i in range(12):
        battery_bank.append(0)  # fill battery with empty cells

    for digit in range(len(line)):
        for battery in range(len(battery_bank)):
            # print(f"battery = {battery}, battery_bank = {int("".join(map(str, battery_bank)))}")
            if is_valid_placement(battery, digit, len(line)):
                if battery_bank[battery] < line[digit]:
                    battery_bank[battery] = line[digit]
                    battery_bank = fill_remainder_with_zeros(battery_bank, battery)
                    break

    joltage = int("".join(map(str, battery_bank)))  # this joins all numbers together in battery list to a single int.
    joltages.append(joltage)

print(joltages)
total_joltage = sum(joltages)
print(total_joltage)


