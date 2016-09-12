import csv
import math

#Calculates root-mean-square-error between two matrices.
def RMSE(a,b):
	su=0
	count=0
	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j]!=-1:
				su+=(a[i][j]-b[i][j])*(a[i][j]-b[i][j])
				count+=1
	rmse=su/count
	rmse=math.sqrt(rmse)
	return rmse

#multiplies 2 matrices.
def matrixmult (A, B):
	C = [[0 for row in range(len(B[0]))] for col in range(len(A))]
	for i in range(len(A)):         
		for j in range(len(B[0])):
			for k in range(len(B)):
				C[i][j] += A[i][k]*B[k][j]
				C[i][j]=round(C[i][j],2)
	return C


#Gets the UV-Decomosition of a matrix. i.e gets 2 matrices 'u' and 'v' such that u*v=input_matrix.
def UV_decom(data):
	error=5
	len1=len(data)
	len2=len(data[0])
	st=0.0
	count=0
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j]!=-1:
				st+=data[i][j]
				count+=1
	#'st' will be the initial value of 'v' and 'u'. st=sqrt(a/d).
	st=st/count
	st=st/15
	st=math.sqrt(st)
	#Initalizing u and v.
	u=[[st for i in range(15)]for j in range(len1)]
	v=[[st for i in range(len2)]for i in range(15)]


	#optimizing U.
	while(True):
		for r in range(len(u)):
			for s in range(len(u[0])):
				a=0
				v2=0
				for j in range(len(v[0])):
					if data[r][j]!=-1:
						total=0
						for k in range(len(v)):
							if k!=s:
								total=total+u[r][k]*v[k][j]
						a=a+v[s][j]*(data[r][j]-total)
						v2=v2+v[s][j]*v[s][j]
				u[r][s]=a/v2

	
		#Optimizing V.
		for r in range(len(v)):
			for s in range(len(v[0])):
				a=0
				u2=0
				for i in range(len(u)):
					if data[i][s]!=-1:
						total=0
						for k in range(len(u[0])):
							if k!=r:
								total=total+u[i][k]*v[k][s]
						a=a+u[i][r]*(data[i][s]-total)
						u2=u2+u[i][r]*u[i][r]
				v[r][s]=a/u2

		
		c=matrixmult(u,v)
		rm=RMSE(data,c)
		#Stop the iteration if RMSE is less than some threshold value.
		if rm<0.1:
			break
		error=rm
	print "\n\nRMSE is :"+str(rm)+"\n\n"
	return c

#main
with open('Movie_Ratings.csv','rb') as f:
	reader=csv.reader(f)
	data1=list(reader)
#Reading the data into a matrix and initialization. 
data=data1[1:]
for i in range(len(data)):
	data[i]=data[i][1:]
	for j in range(len(data[i])):
		if data[i][j]!='':
			data[i][j]=int(data[i][j])
		else:data[i][j]=-1

c=UV_decom(data)
for line in c:
	print line
d=[[0 for i in range(25)]for j in range(25)]

#The difference matrix.
#for i in range(len(data)):
#	for j in range(len(data[0])):
#		if data[i][j]!=-1:
#			d[i][j]=round(data[i][j]-c[i][j],2)
#		else:d[i][j]=-1
#print
#print
#for line in d:
#	print line
