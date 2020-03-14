import numpy as np


def matricize(string):
    r1 = [int(n) for n in string[0:9]]
    r2 = [int(n) for n in string[9:18]]
    r3 = [int(n) for n in string[18:27]]
    r4 = [int(n) for n in string[27:36]]
    r5 = [int(n) for n in string[36:45]]
    r6 = [int(n) for n in string[45:54]]
    r7 = [int(n) for n in string[54:63]]
    r8 = [int(n) for n in string[63:72]]
    r9 = [int(n) for n in string[72:81]]
    
    m = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
    return m


def possible(y,x,n):
    # checks to see if the number exists in the col or row
    global matrix
    for i in range(0,9):
        if matrix[y][i]==n:
            return False
        if matrix[i][x]==n:
            return False
    
    #checks to see if the number exists in the sub-box
    xx = (x//3)*3
    yy = (y//3)*3
    
    for i in range(0,3):
        for j in range(0,3):
            if matrix[yy+i][xx+j]==n:
                return False
        
    return True
        
def solver():
    global matrix
    for y in range(9):
        for x in range(9):
            if matrix[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        matrix[y][x] = n 
                        solver() # recursive step
                        matrix[y][x] = 0
                        
                return
    print(np.matrix(matrix))

if __name__ == '__main__':
    string = input('input the string: \n')
    assert len(str(string))==81
    matrix = matricize(string)
    print('original')
    print(np.matrix(matrix))
    print('\n')
    print('answer')
    solver()