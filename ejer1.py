def sudoku(s):
    sudoku = [
        {0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0,0}]
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