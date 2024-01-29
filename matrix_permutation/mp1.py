import numpy as np

def is_permuation_matrix(x):
    x = np.asanyarray(x)
    return (x.ndim == 2 and x.shape[0] == x.shape[1] and
            (x.sum(axis=0) == 1).all() and
            (x.sum(axis=1) == 1).all() and
            ((x == 1) | (x == 0)).all())


def is_permuation_matrix1(m):
    #Check rows
    if all(sum(row) == 1 for row in m):
        #Check columns
        return all(sum(col) == 1 for col in zip(*m))
    return False

if __name__ == "__main__":
    print('1: ', is_permuation_matrix(np.eye(3)))
    print('2: ', is_permuation_matrix([[0,1],[2,0]]))
    print('3: ', is_permuation_matrix([[0,1],[1,0]]))
    print('4: ', is_permuation_matrix([[0,1,0],[0,0,1],[1,0,0]]))
    print('5: ', is_permuation_matrix([[0,1,0],[0,0,1],[1,0,1]]))
    print('6: ', is_permuation_matrix([[0,1,0],[0,0,1]]))