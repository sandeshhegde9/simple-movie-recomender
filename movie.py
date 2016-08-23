#recomends movies to users depending on their rating.
import csv
from math import sqrt
#calculates cosine distance for two users.
def cosine_distance(user1,user2):
	dist=0
	xy=0
	x2=0
	y2=0
	for key in user1:
		xy+=user1[key]*user2[key] 
		x2+=user1[key]**2        
		y2+=user2[key]**2	
	x2=sqrt(x2)
	y2=sqrt(y2)
	x2=x2*y2
	x2=xy/x2		
	return x2

#Calculates are returns nearest neighbours and their ratings.
def min_dist(username,ratings):
	dist=[]
	for user in ratings:
		if username!=user:
			a=cosine_distance(ratings[username],ratings[user])
			dist.append((user,a))
	return sorted(dist,key=lambda dist:dist[1],reverse=True)

#recomends a set of movies.
def recomend(username,ratings):
	a=min_dist(username,ratings)
	rec=[]
	for movie in ratings[a[0][0]]:
		if ratings[a[0][0]][movie]!=0 and ratings[username][movie]==0:
			rec.append((movie,ratings[a[0][0]][movie]))
	return sorted(rec,key= lambda rec:rec[1],reverse=True)

with open('Movie_Ratings.csv') as f:
    data=[tuple(line) for line in csv.reader(f)]

#Storing the read in dictionary.
ratings={}
for name in data[0]:
	if name!='':
		ratings[name]={}
for i in range(1,len(data)):
	for j in range(1,len(data[i])):
		if data[i][j]!='':
			ratings[data[0][j]][data[i][0]]=int(data[i][j])
		else:ratings[data[0][j]][data[i][0]]=0
a=recomend('Katherine',ratings)
print 'Katherine:'+str(a)
a=recomend('Patrick C',ratings)
print 'patrick c:'+str(a)
a=recomend('Heather',ratings)
print 'heather:'+str(a)
a=recomend('Bryan',ratings)
print 'bryan:'+str(a)


