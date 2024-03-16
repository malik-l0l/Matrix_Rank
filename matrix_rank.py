import numpy as np


def recieve_row_col() -> (int, int):
    """
    receives no_of_rows and no_of_columns from the user.
    :return: no_of_rows, no_of_columns
    """
    while True:
        row = input("No of rows? : ")
        col = input("No of cols? : ")

        if row.isdigit() and col.isdigit():  # validating input
            return int(row), int(col)
        else:
            print("Please enter digits.")


def recieve_2d_matrix(row: int, col: int) -> list:
    """
    receives 2D matrix from the user
    :param row: no_of_rows of the matrix
    :param col: no_of_cols of the matrix
    :return: 2D matrix from the user
    """

    matrix = []
    for i in range(row):
        r = []
        for j in range(col):
            while True:  # to avoid typing/datatype errors.
                x = input(f"matrix[{i}][{j}] ? :")
                if x.isdigit():
                    r.append(int(x))
                    break
        print()
        matrix.append(r)

    return matrix


def find_rank_of_matrix(matrix: list) -> int:
    """
    Finds the rank of the given matrix
    :param matrix: matrix whose rank to be found.
    :return: rank
    """
    return np.linalg.matrix_rank(np.array(matrix))


def print_data(row: int, col: int, matrix: list, rank: int) -> None:
    """
    prints the input data and output data
    :param row: no_of_rows of the matrix
    :param col: no_of_cols of the matrix
    :param matrix: matrix given by the user
    :param rank: calculated rank of given matrix
    :return: None
    """
    print("Matrix : ")
    for i in matrix:
        print(f"\t{i}")

    print(f"\nOrder  : {row}x{col}")

    print(f"Rank   : {rank}")


def main() -> None:
    print("-:: FIND RANK OF THE MATRIX ::-")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    row, col = recieve_row_col()

    print("==========================")

    matrix = recieve_2d_matrix(row, col)

    print("==========================")

    rank = find_rank_of_matrix(matrix)

    print_data(row, col, matrix, rank)

    print("==========================")


if __name__ == '__main__':
    main()

# idk what did I do that day :),I just needed 2 for loop for all this ****.
"""
ask = None
options = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
while ask not in options:
    ask = str(input("what's the order of the matrix? : \n"
                    "a.2x1 b.2x2 c.2x3\n"
                    "d.3x1 e.3x2 f.3x3 g.3x4\n"
                    "h.4x1 i.4x2 j.4x3 k.4x4 l.4x5\n"
                    "m.5x1 n.5x2 p.5x3 q.5x4 r.5x5\n"
                    "ans : ")).lower()
# 2x1
if ask == "a":
    a11 = int(input("a11 : "))
    a21 = int(input("a21 : "))
    my_matrix = np.array([[a11], [a21]])
    print("matrix given in order (2x1) : ")
    for row in my_matrix:
        print(row)
# 2x2
elif ask == "b":
    a11 = int(input("a11 : "))
    a12 = int(input("a12 : "))
    a21 = int(input("a21 : "))
    a22 = int(input("a22 : "))
    my_matrix = np.array([[a11, a12], [a21, a22]])
    print("matrix given in order (2x2) : ")
    for row in my_matrix:
        print(row)
# 2x3
elif ask == "c":
    a11 = int(input("a11 : "))
    a12 = int(input("a12 : "))
    a13 = int(input("a13 : "))
    a21 = int(input("a21 : "))
    a22 = int(input("a22 : "))
    a23 = int(input("a23 : "))

    my_matrix = np.array([[a11, a12, a13], [a21, a22, a23]])
    print("matrix given in order (2x3) : ")
    for row in my_matrix:
        print(row)
# 3x1
elif ask == "d":
    a11 = int(input("a11 : "))
    a21 = int(input("a21 : "))
    a31 = int(input("a31 : "))

    my_matrix = np.array([[a11], [a21], [a31]])
    print("matrix given in order (3x1) : ")
    for row in my_matrix:
        print(row)
# 3x2
elif ask == "e":
    a11 = int(input("a11 : "))
    a12 = int(input("a12 : "))
    a21 = int(input("a21 : "))
    a22 = int(input("a22 : "))
    a31 = int(input("a31 : "))
    a32 = int(input("a32 : "))
    my_matrix = np.array([[a11, a12], [a21, a22], [a31, a32]])
    print("matrix given in order (3x2) : ")
    for row in my_matrix:
        print(row)
# 3x3
elif ask == "f":
    a11 = int(input("a11 : "))
    a12 = int(input("a12 : "))
    a13 = int(input("a13 : "))
    a21 = int(input("a21 : "))
    a22 = int(input("a22 : "))
    a23 = int(input("a23 : "))
    a31 = int(input("a31 : "))
    a32 = int(input("a32 : "))
    a33 = int(input("a33 : "))
    my_matrix = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
    print("matrix given in order (3x3) : ")
    for row in my_matrix:
        print(row)

# 3x4
elif ask == "g":
    a11 = int(input("a11 : "))
    a12 = int(input("a12 : "))
    a13 = int(input("a13 : "))
    a14 = int(input("a14 : "))
    a21 = int(input("a21 : "))
    a22 = int(input("a22 : "))
    a23 = int(input("a23 : "))
    a24 = int(input("a24 : "))
    a31 = int(input("a31 : "))
    a32 = int(input("a32 : "))
    a33 = int(input("a33 : "))
    a34 = int(input("a34 : "))

    my_matrix = np.array([[a11, a12, a13, a14], [a21, a22, a23, a24], [a31, a32, a33, a34]])
    print("matrix given in order (4x4) : ")
    for row in my_matrix:
        print(row)

# 4x1
elif ask == "h":
    a11 = int(input("a11 : "))
    a21 = int(input("a21 : "))
    a31 = int(input("a31 : "))
    a41 = int(input("a41 : "))

    my_matrix = np.array([[a11], [a21], [a31], [a41]])
    print("matrix given in order (4x1) : ")
    for row in my_matrix:
        print(row)
# 4x2
elif ask == "i":
    a11 = int(input("a11 : "))
    a12 = int(input("a12 : "))
    a21 = int(input("a21 : "))
    a22 = int(input("a22 : "))
    a31 = int(input("a31 : "))
    a32 = int(input("a32 : "))
    a41 = int(input("a41 : "))
    a42 = int(input("a42 : "))

    my_matrix = np.array([[a11, a12], [a21, a22], [a31, a32], [a41, a42]])
    print("matrix given in order (4x2) : ")
    for row in my_matrix:
        print(row)
# 4x3
elif ask == "j":
    a11 = int(input("a11 : "))
    a12 = int(input("a12 : "))
    a13 = int(input("a13 : "))
    a21 = int(input("a21 : "))
    a22 = int(input("a22 : "))
    a23 = int(input("a23 : "))
    a31 = int(input("a31 : "))
    a32 = int(input("a32 : "))
    a33 = int(input("a33 : "))
    a41 = int(input("a41 : "))
    a42 = int(input("a42 : "))
    a43 = int(input("a43 : "))

    my_matrix = np.array([[a11, a12, a13],
     [a21, a22, a23],
     [a31, a32, a33],
     [a41, a42, a43]])
    print("matrix given in order (4x3) : ")
    for row in my_matrix:
        print(row)
# 4x4
elif ask == "k":
    a11 = int(input("a11 : "))
    a12 = int(input("a12 : "))
    a13 = int(input("a13 : "))
    a14 = int(input("a14 : "))
    a21 = int(input("a21 : "))
    a22 = int(input("a22 : "))
    a23 = int(input("a23 : "))
    a24 = int(input("a24 : "))
    a31 = int(input("a31 : "))
    a32 = int(input("a32 : "))
    a33 = int(input("a33 : "))
    a34 = int(input("a34 : "))
    a41 = int(input("a41 : "))
    a42 = int(input("a42 : "))
    a43 = int(input("a43 : "))
    a44 = int(input("a44 : "))

    my_matrix = np.array([[a11, a12, a13, a14],
                         [a21, a22, a23, a24],
                         [a31, a32, a33, a34],
                         [a41, a42, a43, a44]])
    print("matrix given in order (4x4) : ")
    for row in my_matrix:
        print(row)

# 4x5

# 5x1

# 5x2

# 5x3

# 5x4
elif ask == "4":
    a11 = int(input("a11 : "))
    a12 = int(input("a12 : "))
    a13 = int(input("a13 : "))
    a14 = int(input("a14 : "))
    a21 = int(input("a21 : "))
    a22 = int(input("a22 : "))
    a23 = int(input("a23 : "))
    a24 = int(input("a24 : "))
    a31 = int(input("a31 : "))
    a32 = int(input("a32 : "))
    a33 = int(input("a33 : "))
    a34 = int(input("a34 : "))
    a41 = int(input("a41 : "))
    a42 = int(input("a42 : "))
    a43 = int(input("a43 : "))
    a44 = int(input("a44 : "))
    a51 = int(input("a51 : "))
    a52 = int(input("a52 : "))
    a53 = int(input("a53 : "))
    a54 = int(input("a54 : "))




# 5x5
elif ask == "4":
    a11 = int(input("a11 : "))
    a12 = int(input("a12 : "))
    a13 = int(input("a13 : "))
    a14 = int(input("a14 : "))
    a15 = int(input("a15 : "))
    a21 = int(input("a21 : "))
    a22 = int(input("a22 : "))
    a23 = int(input("a23 : "))
    a24 = int(input("a24 : "))
    a25 = int(input("a25 : "))
    a31 = int(input("a31 : "))
    a32 = int(input("a32 : "))
    a33 = int(input("a33 : "))
    a34 = int(input("a34 : "))
    a35 = int(input("a35 : "))
    a41 = int(input("a41 : "))
    a42 = int(input("a42 : "))
    a43 = int(input("a43 : "))
    a44 = int(input("a44 : "))
    a45 = int(input("a45 : "))
    a51 = int(input("a51 : "))
    a52 = int(input("a52 : "))
    a53 = int(input("a53 : "))
    a54 = int(input("a54 : "))
    a55 = int(input("a55 : "))

    my_matrix = np.array(
        [[a11, a12, a13, a14, a15], 
        [a21, a22, a23, a24, a25],
        [a31, a32, a33, a34, a35],
        [a41, a42, a43, a44, a45],
        [a51, a52, a53, a54, a55]])
    print("matrix given in order (4x4) : ")
    for row in my_matrix:
        print(row)

rank = np.linalg.matrix_rank(my_matrix)
print(rank)
"""
