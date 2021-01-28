


def matrix_init():
    r = int(input())
    m = []
    for _ in range(r):
        current_row = [el for el in input().split(", ")]
        m.append(current_row)
    return m


matrix = matrix_init()
flat = [int(x) for row in matrix for x in row]
print(flat)