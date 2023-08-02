def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            if column != row[-1]:
                print("{:d}".format(row[i]), end=' ')
            else:
                print("{:d}".format(row[i]), end='')
        print()


