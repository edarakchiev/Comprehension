def matrix_init():
    n = int(input())
    return [[int(el) for el in input().split()] for _ in range(n)]


def check_coordinate(m, r, c):
    if 0 <= r < len(m) and 0 <= c < len(m[r]):
        return True
    print("Invalid coordinates")
    return False


def add_matrix(m, r, c, v):
    if check_coordinate(m, r, c):
        m[r][c] += v
        return m
    return m


def subtract_matrix(m, r, c, v):
    if check_coordinate(m, r, c):
        m[r][c] -= v
        return matrix
    return m


END_COMMAND = "END"
matrix = matrix_init()


while True:
    data = input()
    if data == END_COMMAND:
        break
    command, row, col, value = data.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if command == "Add":
        matrix = add_matrix(matrix, row, col, value)
    elif command == "Subtract":
        matrix = subtract_matrix(matrix, row, col, value)


modified_matrix = [[str(num) for num in e] for e in matrix]
[print(' '.join(el)) for el in modified_matrix]
