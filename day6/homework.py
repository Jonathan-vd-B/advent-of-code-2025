import math

lines: list[list[str]] = []

with open("python/day6/input.txt", "r") as f:
    for line in f:
        current_line: list[str] = []
        for character in line:
            current_line.append(character)
        lines.append(current_line)

# for line in lines:
#     print(line)
#     print(len(line))
# print(len(lines))

operations = lines.pop()
number_of_problems = len([x for x in operations if x != " "])
while len(operations) < len(lines[0]):  # to make sure our operations-list is same length as number rows.
    operations.append(" ")

# for line in lines:
#     print(len(line))
# print(len(operations))

widths_of_problems: list[int] = []
width = 0
for character in operations[1:]:  # [1:] to skip wrong first 0-length entry since first character is operator
    if character == " ":
        width += 1
    else:
        widths_of_problems.append(width)
        width = 0
widths_of_problems.append(width)
# print(widths_of_problems)

total = 0
current_index = 0
for i in range(number_of_problems):
    print(current_index)
    problem: list[int] = []
    width_of_problem = widths_of_problems[i]

    for j in range(width_of_problem):
        number: list[int] = []
        for line in lines:
            if line[current_index + j] != " ":
                number.append(int(line[current_index + j]))
        base = 1
        real_number = 0
        for item in reversed(number):
            real_number += base * item
            base = base * 10
        problem.append(real_number)

    if operations[current_index] == "+":
        total += sum(problem)
    else:
        total += math.prod(problem)

    current_index += width_of_problem + 1  # +1 to bridge 1-width gap between problems

print(total)

# total = 0
# for i in range(len(operations)):
    
#     problem: list[int] = []
#     for j in range(len(problems)):
#         problem.append(problems[j][i])
    
#     if operations[i] == "+":
#         total += sum(problem)
#     else:
#         total += math.prod(problem)

# print(total)