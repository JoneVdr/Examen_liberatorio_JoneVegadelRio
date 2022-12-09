def sudoku(s):
    sudoku = [
        {5,0,0,0,4,0,0,0,9},
        {0,2,0,0,1,0,6,8,0},
        {0,0,9,8,7,0,1,0,0},
        {0,0,6,7,0,0,2,0,0},
        {0,9,0,3,5,4,0,6,0},
        {3,0,0,0,0,0,0,0,1},
        {9,0,0,0,6,0,0,0,2},
        {0,1,4,0,3,0,0,5,7},
        {0,0,5,0,8,7,0,0,0}]
    return sudoku
    print(np.matrix(sudoku))
    for i in range(9):
        if len(set(s[i])) != 9:
            return False
    for i in range(9):
        if len(set([s[j][i] for j in range(9)])) != 9:
            return False
    for i in range(3):
        for j in range(3):
            if len(set([s[3*i+k][3*j+l] for k in range(3) for l in range(3)])) != 9:
                return False
    return True