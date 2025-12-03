import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]  : 


    b_row= len(a)    #rows
    b_col = len(a[0]) #cols
    b=[]

    # Transposing logic
    for i in range(b_col) :
        t=[]
        for j in range(b_row) :
            t.append(a[j][i])
        b.append(t)


    return b  
    # trans =  np.array(a).transpose() or np.array(a).T
    # return trans.tolist()

if __name__ == "__main__" :

        row = int(input("Enter number of rows : - "))
        col = int(input("Enter number of columns : - "))

        matrix = [] 
        print("Enter elements(matrix) row-wise ")
        for i in range(row) :

            r =[]
            for j in range(col) :
                r.append(float(input(f"Enter the elements at ({i},{j}) - ")))
            matrix.append(r)

        print("Matrix before transposing : - ")
        for i in matrix :
            print(i)


        trans = transpose_matrix(matrix) 
        print(f"Transposed Matrix : - ")
        for i in trans :
            print(i)




# a = [[1,2,3],
#     [4,5,6]]
# function i/p parameter is(2d-matrix)_of type (int/float) and also_expects_in_same format(o/p)