import numpy as np

class soln : 

    def reshape_matrix(self , a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]] :


        if len(a[0])*len(a) == new_shape[0]*new_shape[1] :           # total_area_mustmatch to reshape_matrix

            r  , op = [] ,[]
            for i in range(len(a)) :           # flattened_list to extract_value directly
                for j in range(len(a[1])) :
                    r.append(a[i][j])
                
            for i in range(new_shape[0]) :             # creating_matrix of shape - of_the tuple
                ri=[]
                for j in range(new_shape[1]) :
                    ri.append(0)
                op.append(ri)

            k = 0
            for i in range(len(op)) :       
                
                for j in range(len(op[0])) :
                    op[i][j]  =  r[k]        
                    k+=1
            return op
        
        else :
            return []
        

        # res=[]                                  using numpy's reshape
        # if len(a[0])*len(a) == new_shape[0]*new_shape[1] :
        #     a=np.array(a)
        #     res = np.reshape(a,new_shape)

        # else :
        #     return res  
        
        # return res.tolist()
    
       
if __name__ == "__main__" : 

    a =  [[1, 2, 3, 4], [5, 6, 7, 8]]
    b =  (1, 4)

    ri = soln()
    print(f"Reshaped Matrix - {ri.reshape_matrix(a,b)}")



# Multiplication(matmul): Inner dimensions must match.
# Reshape: Total product (area) must match