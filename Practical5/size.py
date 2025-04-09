 #Define population data for UK countries and Chinese provinces.
 #Sort the population data.
 #Define corresponding labels for each region.
 #Create a figure with two subplots (side by side).
 #Plot a pie chart for UK countries with labels and percentages.
 #Set the title for the UK pie chart.
 #Plot a pie chart for Chinese provinces with labels and percentages.
 #Set the title for the China pie chart.
 #Display the charts.import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
uk_countries=[57.11,3.13,1.91,5.45]
china_province=[65.77,41.88,45.28,61.27,85.15]
uk=sorted(uk_countries)
china=sorted(china_province)
uk_country=["Northern Ireland","Wales","Scotland","England"]
china_province=["Fujian","Jiangxi","Anhui","Zhejiang","Jiangsu"]
plt.figure(1)
plt.subplot(1,2,1)
plt.pie(uk,labels=uk_country,autopct="%.2f%%",)
plt.title("UK Countries Distribution")
plt.subplots_adjust(top=1,bottom=0)
plt.legend(loc=2,fontsize=5)
plt.subplot(1,2,2)
plt.pie(china,labels=china_province,autopct="%.2f%%")
plt.title("China Province Distribution")
plt.legend(loc=1,fontsize=5)
print(f"uk_country distribution is {uk}")
print(f"china_province distribution is {china}")
plt.show()