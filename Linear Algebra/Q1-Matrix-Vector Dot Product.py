import numpy as np

class adhoc :

    def matrix_dot_vector( self , a: list[list[int|float]] ,b : list[list[int|float]] ) -> list[int|float] :

        # vic =[]
        if(len(a[0]) == len(b))  :           # if len(col) , dont match -1,as we_are traversing rowise

            # for i in range(len(a)) :
            #     sum=0
            #     for j in range(len(a[0])) :
            #         sum+= a[i][j]*b[j]
            #     vic.append(sum)

            a , b= np.array(a) , np.array(b)
            vic = a @ b    #np.dot(a,b)           this also supports matr-vector
 
        else :
            return -1

        return vic.tolist()


if __name__ == "__main__" :

    a , vec = [[1, 2], [2, 4]] , [] 
    inp = input("Enter vector elements sepr_by space - ").split()

    for i in range(len(inp))  :
        vec.append(float(inp[i]))

    ad=adhoc()
    print(f"Matrix-Vector Dot Product :- {ad.matrix_dot_vector(a,vec)}")