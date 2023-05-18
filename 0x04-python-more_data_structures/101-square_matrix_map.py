#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda kl: list(map(lambda v: v**2, kl)), matrix))
