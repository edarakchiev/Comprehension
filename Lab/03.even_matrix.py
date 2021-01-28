def str_to_int(strs):
    return [int(x) for x in strs]


def matrix_init():
    r = int(input())
    return [str_to_int(input().split(", ")) for _ in range(r)]


def get_even_matrix(mat):
    return [[x for x in row if x % 2 == 0] for row in mat]


def print_matrix(matr):
    print(matr)


matrix = matrix_init()
even_matrix = get_even_matrix(matrix)
print_matrix(even_matrix)
