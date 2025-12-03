import numpy as np

def calculate_dot_product(vec1, vec2) -> float:  
    
    cnt=0
    for i in range(len(vec2)) :        # multiply same index values_ofmatrix
        cnt+=vec1[i]*vec2[i]

    return cnt 
    #return np.dot(vec1,vec2)

if __name__ == "__main__" :
	

    vector1 = input("Enter values for vec1 seperated by_space : - ").split()             # by_default_takeswhite_space
    vector2 = input("Enter values for vec2 seperated by_space : - ").split()

    vector1 = np.array(vector1,dtype=float) 
    vector2  = np.array(vector2,dtype=float) 
    print(f"Vector1 -{vector1}")
    print(f"Vector2 -{vector2}")

    cnt = calculate_dot_product(vector1 ,vector2)
    print(f"Dot Product of_two vectors : {cnt}")


# dot product (also known as_scalar product) of two vectors,must be of the same size(dimn)