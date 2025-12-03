import numpy as np

class soln :

	def calculate_matrix_mean(self ,matrix: list[list[float]], mode: str) -> list[float]:
			
		# row=len(matrix)
		# col = len(matrix[0])
		# b=[]
		# if mode == "row" :
		# 	for i in range(row) :
		# 		g=0
		# 		for  j in range(col) :
		# 			g+=matr[i][j]

		# 		b.append(g/len(matr[0]))           # mean across row
		# 	return b

		# elif mode == "col" :
		# 	for i in range(col) :
		# 		g=0
		# 		for  j in range(row) :
		# 			g+=matr[j][i]

		# 		b.append(g/len(matr))           # mean across column
		# 	return b

		if mode == "row" :
			res = np.array(matrix).mean(axis=1)     # across mean
		elif  mode == "col" :	
			res = np.array(matrix).mean(axis=0)     # across col
		else :
			raise ValueError("Mode must be row or col")
		
		return res.tolist()

if __name__ == "__main__" :

	row = int(input("Enter row of matrix sepr_byspace :  "))
	col  = int(input("Enter coln of matrix sepr_byspace :  "))

	mode = input("Enter row or col to perform mean operation : ")
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

	out = soln() 
	print(f"Mean according to the specified mode is - {out.calculate_matrix_mean(matr,mode)}  ")
	