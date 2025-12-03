import numpy as np

class trn :
    import numpy as np

    # def multp(self,J: list[list[int|float]], K: list[list[int|float]]) -> list[list[int|float]]:

    #     c = [ 
    #         [J[0][0]* K[0][0] + J[0][1]*K[1][0]
    #          , J[0][0]* K[0][1] + J[0][1]*K[1][1]] ,

    #         [J[1][0]* K[0][0] + J[1][1]*K[1][0],
    #           J[1][0]* K[0][1] + J[1][1]*K[1][1] ]
    #     ]
    #     return c 

    def transform_matrix(self , A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

        # det = T[0][0]*T[1][1] - (T[0][1]*T[1][0])
        # # t det not zero then perform op's
        # if det !=0 :

        #     # converted to T^(-1) 
        #     T[0][0] , T[1][1] = (T[1][1])/det , (T[0][0])/det     
        #     T[0][1] , T[1][0] =  -T[0][1]/det , -T[1][0]/det

        #     b = self.multp(T,A)

        #     res = self.multp(b,S) 

        #     return res


        # else :
        #     return -1        # singular matrix

        T = np.array(T)
        A = np.array(A)
        S = np.array(S)
        det_t = np.linalg.det(T)
        det_s = np.linalg.det(S)
        Tinv = np.linalg.inv(T)

        if (det_t and det_s) != 0 :
            ans = Tinv @ A @ S
            return ans.tolist()    
        
        else :
            return -1

if __name__ == "__main__" :

    A = [[1, 2], [3, 4]]
    T = [[2, 0], [0, 2]]
    S = [[1, 1], [0, 1]]

    o=trn()
    print(f"Matrix Transformation using operation (T⁻¹AS) - {o.transform_matrix(A,T,S)}")











