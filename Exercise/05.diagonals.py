def str_to_int(strs):
    return [int(x) for x in strs]


def int_to_str(ints):
    return [str(x) for x in ints]


def matrix_init():
    n = int(input())
    return [str_to_int(input().split(", ")) for _ in range(n)], n


def second_diagonal(m):
    r = 0
    s = len(m)
    diagonal = []
    for e in range(s-1, -1, -1):
        diagonal.append(m[r][e])
        r += 1
    return diagonal


matrix, size = matrix_init()

first_diagonal = [matrix[x][x] for x in range(size)]
second_diagonal = second_diagonal(matrix)
print(f"First diagonal: {', '.join(int_to_str(first_diagonal))}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(int_to_str(second_diagonal))}. Sum: {sum(second_diagonal)}")
