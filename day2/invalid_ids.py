collection: list[list[int]] = []
with open("python/day2/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        ranges = line.split(",")
        for range_pair in ranges:
            range_: list[int] = []
            bounds = range_pair.split("-")
            start = int(bounds[0])
            end = int(bounds[1])
            range_length = end - start + 1  # include start
            for i in range(range_length):
                range_.append(start + i)
            collection.append(range_)
# print(collection)

invalid_IDs: list[int] = []

for range_ in collection:
    start = range_[0]
    end = range_[-1]
    # print(range_, start, end)
    for i in range(end - start + 1):  # include the end
        # print(start + i)
        number = start + i 
        str_number = str(number)

        highest_sequence: float = len(str_number) / 2
        sequence_number = ""
        for sequence in range(int(highest_sequence)):
            sequence_number = sequence_number + str_number[sequence]
            
            # repeat sequence till same lenght as original number and compare made and original. If same, its invalid ID.
            madeup = ""
            for i in range(len(str_number) // (sequence + 1)):
                madeup = madeup + sequence_number
            if madeup == str_number:
                print(f"Invalid even ID {number} found!")
                invalid_IDs.append(number)
                break
            
                

sum = 0
for id_ in invalid_IDs:
    sum += id_

print(f"\nsum of all invalid IDs = {sum}")
       
