import numpy as np
class mat :
    
    def matrixmul(self , a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:

        row = len(a)
        col=len(b[0])
        inner = len(b)         #len(a[0])
        res=[]
# creating matrix_of_size len(a) * len(b[0])

        for i in range(row) :
            r=[]
            for j in range(col) :
                r.append(0)
            res.append(r)                  # i.elist_of_list

        if(len(a[0]) == len(b)) :       # valid_dimn's
            # main_multp_logic

            for i in range(row) :             # the row(of matA) for resultant
                for j in range(col) :          # cols of (matB) for resultant

                    for k in range(inner) :     # to go deeper we need _row(matB)or col(matA)which_aresame_byrule
                        res[i][j] += a[i][k] * b[k][j]

            return res
            # a=np.array(a)
            # b=np.array(b)
            # c=np.matmul(a,b)
        else :
            return -1 


        
if __name__ == "__main__" :
    
    mat1 = [ [1, 4, 2],
            [0, -3, 5] ]
    mat2 = [ [2, 3, 1, 4],[6, 0, 7, 2],[-1, 8, 3, 5] ]
    obj = mat()
    print(f"Matrix times Matrix - {obj.matrixmul(mat1,mat2)}")




# matrix multp C=A⋅B only if both_matrix size(align's)
# means col(mat1) == row(mat2) 