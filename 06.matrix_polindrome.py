r, c = [int(num) for num in input().split()]
matrix = []
start = 97
for row in range(r):
    current_row = []
    for col in range(c):
        el_1 = chr(start + row)
        el_2 = chr(start + row + col)
        current_row.append(el_1 + el_2 + el_1 )
    matrix.append(current_row)


for e in matrix:
    print(*e)
