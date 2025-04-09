import numpy as np
import matplotlib.pyplot as plt
#initialize
population=10000
S=population-1
I=1
R=0
beta=0.3
gamma=0.05
time=1000
#Create lists to store results
S_list=[S]
I_list=[I]
R_list=[R]
time_array=np.array(range(0,time+1))

#Compute infection probability
#Determine new infections
#Determine new recoveries
#Update S, I, R values and store them in list
for _ in range(0,time):
    i_prob=beta*I/population
    new_I=sum(np.random.choice(range(2),S,p=[1-i_prob,i_prob]))
    new_R=sum(np.random.choice(range(2),I,p=[1-gamma,gamma]))
    S-=new_I
    R+=new_R
    I+=new_I-new_R
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

#plot the figure
plt.figure(figsize=(6, 4), dpi=150)
line1=plt.plot(time_array,S_list,color="blue",label="susceptible")
line2=plt.plot(time_array,I_list,color="orange",label="infected")
line3=plt.plot(time_array,R_list,color="green",label="recovered")
plt.xlabel("Time")
plt.ylabel("number of people")
plt.title("SIR model")
plt.legend(loc=1)
plt.savefig('SIR.png', format='png')
plt.show()