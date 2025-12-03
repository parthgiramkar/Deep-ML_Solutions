import numpy as np

class cla :

    def inverse_2x2(self ,matrix : list[list[int|float]]) -> list[list[int|float]] :

        # det = matrix[0][0]*matrix[1][1] - (matrix[0][1]*matrix[1][0])        # determinant
        # if det != 0 :

        #     matrix[0][0] ,  matrix[1][1] = (matrix[1][1])/det , (matrix[0][0])/det     # swappin_val's with its minor 
        #     matrix[0][1] , matrix[1][0] =  -matrix[0][1]/det , -matrix[1][0]/det 

        #     return matrix

        # else :
        #     return -1      # singular_matrix
        inverse= np.array(matrix)
        det = np.linalg.det(inverse)

        if det != 0 :
            m = np.linalg.inv(inverse)
            m=np.round(m,2)
            return m.tolist()
        else :
            return -1


if __name__ == "__main__" :

    a = [[4, 7], [2, 6]] 
    io = cla()
    print(f"Inverse of a 2x2 matrix - {io.inverse_2x2(a)}")




# matrix inverse - A*A^(-1) = I , where is identity_matrix
# only when its square matrix(same number of rows and columns)
# and determinant is not zero (det(A) ≠ 0) ,means matrix should not be singular

# for 2x2 matrix A=[ab
#                   ​cd​]
# INVERSE - A^(−1)=1* [d -b
#                     -c  a] /(ad−bc)     (determinant)