


def rotate(matrix):
    """Rotates the square matrix.
    0,0
    1,0 0,1
    2,0 1,1 0,2
    2,1 1,2
    2,2
    """
    i = j = k = 0
    for k in range(len(matrix)):
        i = k
        j = 0
        while i >= 0:
            print matrix[i][j],
            i = i - 1
            j = j + 1
        print "\n"

    # print the lower half.
    for k in range(len(matrix) - 1):
        j = k + 1
        i = len(matrix) - 1
        while i > k:
            print matrix[i][j],
            i = i - 1
            j = j + 1
        print "\n"
        

if __name__ == "__main__":
    matrix = [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"]
    ]

    rotate(matrix)
