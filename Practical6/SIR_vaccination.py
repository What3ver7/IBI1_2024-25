import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#initialize
population=10000
percentage=[i for i in range(0,101,10)]
beta=0.3
gamma=0.05
time=1000
color=["green","blue","red","pink","cyan","grey","yellow","orange","purple","black","brown"]
time_array=np.array(range(0,time+1))
#loops for range(0,101,10)
#Create lists to store results
for i in percentage:
    I=1
    R=0
    i_index=percentage.index(i)
    I_list=[I]
    R_list=[R]
    V=population*i/100
    S=population-1-V
    S_list=[S]
    #loops for range(0,time)
    #Compute infection probability
    #Determine new infections
    #Determine new recoveries
    #Update S, I, R values and store them in list
    for _ in range(0,time):
        if I==0:
            S_list.append(S)
            I_list.append(I)
            R_list.append(R)
            continue
        elif V==population:
            S_list.append(S)
            I_list.append(I)
            R_list.append(R)
            continue
        i_prob=beta*I/population
        new_I=sum(np.random.choice(range(2),int(S),p=[1-i_prob,i_prob]))
        new_R=sum(np.random.choice(range(2),int(I),p=[1-gamma,gamma]))
        S-=new_I
        R+=new_R
        I+=new_I-new_R
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
    line=plt.plot(time_array,I_list,color=cm.viridis(i*4),label=f"{percentage[i_index]}%")
##plot the figure
plt.xlabel("Time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend(loc=1,fontsize=8)
plt.savefig ("SIR_vaccination.png")
plt.show()
