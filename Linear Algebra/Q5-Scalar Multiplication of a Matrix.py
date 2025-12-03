import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

	# result=[]
	# for i in range(row) :
	# 	r=[]
	# 	for j in range(col) :
	# 		res = scalar*matrix[i][j]
	# 		r.append(res)
	# 	result.append(r)

	result = np.array(matrix)*scalar

	return result.tolist()

if __name__ == "__main__" :

	row = int(input("Enter row of matrix sepr_byspace :  "))
	col  = int(input("Enter coln of matrix sepr_byspace :  "))

	scal = float(input("Enter Scalar_value to multiply with : "))
	matr = []
	for i in range(row) :
		res=[]
		for  j in range(col) :
			g=float(input(f"Enter element at {i,j} - "))
			res.append(g)
		matr.append(res)

	print("Given Matrix : -")
	for i in matr :
		print(i)	

	print("Scalar Multiplication of Matrix : - ")	
	out = scalar_multiply(matr,scal)
	for i in out :
		print(i)