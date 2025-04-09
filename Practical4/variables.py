#4.1
a=15 # The walk to the bus stop is 15 mins
b=75 # The bus journey takes 1 hr and 15 mins
c=a+b # Store the total length of time for this commute in a third variable
d=90 #The drive takes 1 hr and 30 mins
e=5
f=d+e
# Because c=90<f=95, so the first way is fatser.

#4.2
X=True
Y=False
W=X and Y
print("W:",W)
#  X  |   Y   |  W=X and Y | X or Y
# True| False |   False    | True   
# True| True  |   True     | True
# False|True  |   False    | True
# False|False |   False    | False