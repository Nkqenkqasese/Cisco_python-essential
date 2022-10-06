					#SCENARIO

#Write a function that creates and print the simpliest tridiagonal matrix (unique values for sub/supr diagonal and diagonal)
#test it with different values for the sub diagonal, the diagonal and supra diagonal

import numpy as np

global size
global sub_diag
global diag
global supr_diag

def tridiag_matrix(size,sub_diag,diag,supr_diag):

	matrix=[]
	lignes_i_matrice = []
	ligne_1_matrice = [diag,supr_diag]
	ligne_n_matrice = [sub_diag,diag]
	n = size

#Build the first line of the matrix by concanating [diag,upp diag] with n-2 0

	for i in range(n-2):
		ligne_1_matrice.append(0)
	matrix.append(ligne_1_matrice)

#Build the inside lines of the matrix from 2 to n-1
	for i in range(n):
		lignes_i_matrice.append(0) #create a line with n 0
	for i in range(0,n-2):
		lignes_i_matrice[i]=sub_diag #the i° 0 of the line is equal to sub_diag
		lignes_i_matrice[1+i]=diag  #the i+1° 0 of the line is equal to diag
		lignes_i_matrice[2+i]=supr_diag  #the i+2° 0 of the line is equal to upp_diag
		stock_lignei = lignes_i_matrice[:]
		matrix.append(stock_lignei) #store the line in the matrix
		for j in range(len(lignes_i_matrice)):
			lignes_i_matrice[j]=0

#Build the last line of the matrix by concatenating n-2 0 with  [sub_diag,diag]
	for i in range(n-2):
		ligne_n_matrice.insert(0, 0)
	matrix.append(ligne_n_matrice)

	matrix_final = np.array(matrix)
	return(matrix_final)

n = int(input('Input the size of the matrice: '))
x = int(input('Input the unique value for the sub diagonal : '))
y = int(input('Input the unique value for the diagonal : '))
z = int(input('Input the unique value for the supra diagonal : '))
print(tridiag_matrix(n,x,y,z))




