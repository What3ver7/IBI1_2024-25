 #Import `matplotlib.pyplot` as `plt`.  
 #Create a dictionary of languages and their popularity percentages.  
 #Extract keys (languages) and convert percentage values to floats.  
 #Plot a bar chart with `plt.bar()`.  
 #Set y-axis ticks from 0 to 100 with intervals of 10.  
 #Add percentage labels above each bar.  
 #Label x-axis, y-axis, and set the title.  
 #Display the chart using `plt.show()`.  
 #ask for user's input
import matplotlib.pyplot as plt
dict={"TypeScript":"38.5%",
      "SQL":"51%",
      "Python":"51%",
      "HTML":"52.9%",
      "JavaScript":"62.3%",
       } 
x=list(dict.keys())
y =[float(value.strip('%')) for value in dict.values()]
plt.bar(x,y)
plt.yticks(range(0,100,10))
for i, value in enumerate(y):
    plt.text(i, value, f"{value}%",ha="center", va="bottom")
plt.xlabel("Application")
plt.ylabel("Percentage")
plt.title("Programming language popularity")
plt.show()
x=input("which language?")
if x in dict:
    print(f"the percentage of developers who use this language is {dict[x]}")
else:
    print("language not found.")
