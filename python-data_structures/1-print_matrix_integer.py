def print_matrix_integer(matrix=[[]]):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0

    # Iterate through each row and print the elements separated by tabs
    for row in matrix:
        for col_index, value in enumerate(row):
            # Print the integer value with tab separation using str.format()
            print("{:d}".format(value), end="\t")
