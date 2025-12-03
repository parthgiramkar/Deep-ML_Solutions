import numpy as np
class krn :

    def linear_regression_normal_equation(self , X: list[list[int|float]] , y : list[int|float] ) -> list[float]  :
        
# here , the bias is already added_inquestion_itself so no,need to add it  
   
        # ones = np.ones( (len(X) , 1) )            # same as_size of i/p matrix X(features) and col1 for bias
        X , y = np.array(X) , np.array(y)
        # ones = np.concatenate( (ones,X) , axis=1)           # concatenate values colwise
        
        theta = X.transpose() @  X 
        det = np.linalg.det(theta)
        if det !=0 :
            theta = np.round(np.linalg.inv(theta) @  X.transpose() @ y , 4)
            return theta.tolist()
        
        else :
            return -1


if __name__ == "__main__" :


    x = [[1, 3, 4], [1, 2, 5], [1, 3, 2]] 
    y = [1, 2, 1]

    ho = krn()
    print(f"Coefficients of the linear regression model - {ho.linear_regression_normal_equation(x,y)}")



# Formula - theta = (X^T X)^{-1} X^T y 
# here theta is_representing column vector - where there's only one col and the row are weights(of_eachfeature) 
# putting in this equation - lets,say : - y = theta_not(1) + \theta_1({KM}) + \theta_2({Age}) , we get the y_pred for each i/p of x 

# the no.of values in theta is equal to - no.of cols(representingeach_feature) in_i/p_matrix after concatenating  
# for bias to represent , we concatenate one col - of_1's 