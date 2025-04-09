# set sum to 0
# define n as [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# create an empty list called list

# for each element i in n 
#  add i to sum
#    append sum to list

#Set newlist as a list of integers from 1 to 10  
#Set sum as 0  
#Set list as an empty list  

#For each element i in newlist:
#  Add i to sum  
#  Append sum to list  
#Print list  


newlist=[x for x in range(1,11)]
sum=0  
list=[]
for i in newlist:
    sum+=i  
    list.append(sum) 
print(list) 