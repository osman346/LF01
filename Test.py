matrix = []
value = 0
for x in range(1, 6):
    row = []
    for y in range(1, 4):
        row.append(value)
        value += 1
    matrix.append(row)
print(matrix)