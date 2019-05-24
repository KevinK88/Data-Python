import csv
from matplotlib import pyplot as plt
from datetime import datetime
# Read data from the file
filename = 'sitka_weather_07-2014.csv'
with open(filename) as file:
	reader = csv.reader(file)
	header_row = next(reader)
	dates =[]
	lows = []
	highs =[]

#Get data from Date, Max and Min temperature
#Use Exception to catch error
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],"%Y-%m-%d")
			high = int(row[1])	
			low = int(row[3])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date) 
			highs.append(high) 
			lows.append(low)
fig = plt.figure(dpi = 128, figsize =(10,6))

plt.plot(dates,highs,c='red',alpha =0.5)
plt.plot(dates,lows,c='blue',alpha =0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
title = "Max and Min Temperature"
plt.title(title,fontsize = 24)
plt.ylabel('Temperature (F)',fontsize = 15)
fig.autofmt_xdate()
plt.tick_params(axis ='both',which ='major',labelsize = 16)
plt.show()
