import numpy as np

def linear_regression_gradient_descent( X : np.ndarray , y: np.ndarray , alpha : float , iterations : int ) -> np.ndarray   :

    col = len(X[0])
    row = len(X)            # no.of samples/data for training

    theta = np.zeros( (col ,1) )        # setting b&m initial to zero
    y = y.reshape( (-1,1))                 # making single_list to coln-vector for subtraction 

    for i in range(iterations)   :       # training_to_given_no.of iter's to get optimal b,m

        y_pred = X @ theta             # the equ_in matrix form - mxi + b

        error = y_pred - y               # reverse_to move_our negative(in_calc)

        gradient = (X.transpose() @ error)*2/row         # in_calulus its grad is_our derivative and x_transpose is_our summation
        theta = theta - (alpha*gradient)        # subtract_as we need to reach_bottom_towards_min_error_loss
    
    return np.round(theta.flatten(),4)          # flatten - into_a_single_list


if __name__  == "__main__" :

    X = np.array([[1, 1, 0], [1, 2, 1], [1, 3, 2], [1, 4, 3]]) 
    y = np.array([5, 6, 7, 8]) 
    alpha  , iterations = 0.01 , 1000
    
    print(f"Coefficients of the linear regression model - {linear_regression_gradient_descent(X,y,alpha,iterations)}")



# theta dimension,is coln vector where one col and rows = no.of feature cols in i/p matrix

# in reshaping(-1) means total_elem/cols = rows , 