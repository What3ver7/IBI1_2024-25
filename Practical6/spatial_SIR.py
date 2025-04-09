import numpy as np
import matplotlib.pyplot as plt

#define the population
#Randomly choose the initial infected individual's position
population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
beta=0.3
gamma=0.05
time=100

#draw the initial figure
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap="viridis",interpolation="nearest")
plt.title("Initial")
plt.savefig("day0.png")
plt.show()

#loop for 100 times
#infect the neighboring susceptible individuals
#let the infected individuals recover 
for i in range(1,time+1):
    new_population = np.copy(population)
    infect=np.where(population==1)
    for j in range(len(infect[0])):
        x,y=infect[0][j],infect[1][j]
        for x_change in range(-1,2):
            for y_change in range(-1,2):
                x_side,y_side=x+x_change,y+y_change
                if 0<=x_side<100 and 0<=y_side<100 and population[x_side,y_side]==0:
                    new_population[x_side,y_side]=np.random.choice(range(0,2),1,p=[1-beta,beta])
        new_recover=np.random.choice(range(1,3),1,p=[1-gamma,gamma])
        new_population[x,y]=new_recover
    population=new_population
    #draw the figure at 10,50,100 day
    if i in [10,50,100]:
        plt.imshow(population,cmap="viridis",interpolation="nearest")
        plt.title(f"day {i}")
        plt.savefig (f"day{i}.png")
        plt.show()

# Start by creating a 100x100 grid where every spot is empty (0).
# Pick a random spot and mark it as infected (1).
# Decide how likely it is for the infection to spread (beta) and for someone to recover (gamma).
# Set the simulation to run for 100 days.
# Show the figure at the start with just the one infected spot.
# For each of the 100 days:
#    Make a copy of the grid to update.
#    Look for infected spots (1).
#    For each infected spot:
#        For each direction (up, down, left, right):
#            If there's an open spot next to it:
#                Sometimes turn it infected (based on beta).
#        Sometimes turn the infected spot recovered (based on gamma).
#    Update the grid with the changes.
#    If it's a special day (10, 50, or 100), draw the figure to show how it looks now.