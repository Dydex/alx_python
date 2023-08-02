def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print()
        for i in range(0, len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]))
            else:
                print("{:d}".format(row[i]), end=" ")

