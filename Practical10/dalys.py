#Import necessary libraries: os, pandas, matplotlib.pyplot, numpy.
#Set the current working directory to the folder containing the data file.
#Print the current working directory and list all files in it.
#Load the dalys-rate-from-all-causes.csv file into a DataFrame called dalys_data.
#Print the first five rows of dalys_data to understand the structure.
#Print data type info of each column in the DataFrame.
#Print statistical description of numerical columns (especially DALYs and Year).
#Print the 'Year' column for the first 10 rows of the DataFrame.
#Extract and print the 10th year DALYs was recorded in Afghanistan (based on row index).
#Filter the DataFrame for rows where 'Year' is 1990, extract the 'DALYs' column and print it.
#Extract rows for the United Kingdom and France into separate DataFrames.
#Calculate the mean DALYs for both the UK and France.
#Print the mean DALYs for both countries.
#Compare the mean DALYs between the UK and France:
#If the UK mean is higher, print "UK has more DALYs."
#Otherwise, print "France has more DALYs."
#Plot DALYs over time for the UK using a '+' marker:
#Set title, x-label, y-label, rotate x-ticks, and add a legend.
#Filter data for China.
#Create a plot with both China's and the UK's DALYs over the years:
#Use different line styles and colors for distinction.
#Set title, x-label, y-label, rotate x-ticks, and add a legend.
#Display both plots.
#(Commentary) Observe that DALYs for both China and the UK show a decreasing trend over time.

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("D:\IBI1\IBI1_2024-25")
print("Current working directory:", os.getcwd())
print("The files in directory:", os.listdir())
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print("The satistics in the first five lows: ")
print(dalys_data.head(5))
print("\nThe type information of the satistics: ")
print(dalys_data.info())
print("\ninformations about year and DALYs:")
print(dalys_data.describe())

print("\nThe years:")
print(dalys_data.iloc[0:10,2])
print("the 10th year for which DALYs were recorded in Afghanistan", dalys_data.iloc[9,2])
#the 10th year for which DALYs were recorded in Afghanistan is 1999

dalysin1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
print("\nThe DALYs in 1990:")
print(dalysin1990)

uk=dalys_data.loc[dalys_data["Entity"]=="United Kingdom", ["DALYs", "Year"]]
france=dalys_data.loc[dalys_data["Entity"]=="France", ["DALYs", "Year"]]
uk_mean=uk["DALYs"].mean()
france_mean=france["DALYs"].mean()
print("\nThe mean of uk dalys",uk_mean)
print("The mean of france dalys",france_mean)
if uk_mean >france_mean:
    print("uk is more than france in dalys.")
else:
    print("france is more than uk in dalys.")
#uk is more than france in dalys, uk is around 23319, france is around 21475.

plt.plot(uk["Year"], uk["DALYs"], 'b+', label="United Kingdom")
plt.title("DALYs in the United Kingdom")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(uk["Year"], rotation=-90)
plt.legend()
plt.show()


china=dalys_data.loc[dalys_data["Entity"]=="China", ["DALYs", "Year"]]
plt.plot(china["Year"], china["DALYs"], 'r-', label="China")
plt.plot(uk["Year"], uk["DALYs"], 'b+', label="United Kingdom")
plt.title("DALYs between the United Kingdom and China")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(china["Year"], rotation=-90)
plt.legend()
plt.show()
#The change between China and UK is more similar, both of their dalys are decreasing in the period.
