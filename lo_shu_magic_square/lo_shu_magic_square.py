def main():
    square = [[4, 9, 2],
              [3, 5, 7],
              [8, 1, 6]]
    print(is_magic_square(square))

def is_magic_square(lst):
    values = []

    # Check if 2D list is a 3x3 matrix.
    if len(lst) != 3:
        return False
    else:
        for r in range(len(lst)):
            if len(lst[r]) != 3:
                print("Failed in 3x3 matrix check.")
                return False

    # Check if square has duplicates
    for r in range(3):
        for c in range(3):
            if lst[r][c] in values:
                print("Failed in duplicates check.")
                return False
            else:
                values.append(lst[r][c])

    # Check if square has values exactly between 1-9
    for val in values:
        if val < 1 or val > 9:
            print("Failed in 1-9 exactly check.")
            return False

    # List to hold row sums, column sums, and diagonal sums
    sums = []

    # Check if rows add up to the same number
    for r in range(3):
        row_sum = 0
        for c in range(3):
            col_val = lst[r][c]
            row_sum += col_val
        if len(sums) == 0:
            sums.append(row_sum)
        elif row_sum not in sums:
            print("Failed in row sum check.")
            return False

    # Check if columns add up to the same number as rows
    for c in range(3):
        col_sum = 0
        for r in range(3):
            row_val = lst[r][c]
            col_sum += row_val
        if col_sum not in sums:
            print("Failed in column sum check.")
            return False

    # Check if diagonal 1 adds up to the same number as columns and rows
    diag1_sum = lst[0][0] + lst[1][1] + lst[2][2]
    if diag1_sum not in sums:
        print("Failed in diagonal 1 sum check.")
        return False
    else:
        sums.append(diag1_sum)

    # Check if diagonal 2 adds up to the same number as columns and rows
    diag2_sum = lst[0][2] + lst[1][1] + lst[2][0]
    if diag2_sum not in sums:
        print("Failed in diagonal 2 sum check.")
        return False
    else:
        sums.append(diag2_sum)

    # Square passes all checks and is a magic square
    return True

main()
