import numpy as np
#load the csv file: befkbhalderstatkode.csv into a numpy ndarray
filename = './befkbhalderstatkode.csv'
data = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
#print(data)

#How many german children were 0 years old in 2015?
mask = (data[:,0] == 2015) & (data[:,2] == 0) & (data[:,3] == 5180)
print('German children - 0 year old in 2015:', data[mask])

#create a function that can take any combination of the 4 parameters:AAR,BYDEL,ALDER,STATKODE and return population data

#create a new function like previous so that it can sum values for all ages if age is not provided to the function
#further add functionality to sum values if citizenship or area was not provided to function.
#create a new function that can also give average values for each year if year whas not provided.
#create a function, that given year and nationality can return which area had the most of these nationals by that year. Test it by finding out which area had the most Moroccan people in both 1992 and 2015
#Find the Area(s) where fewest foreingers lived in Copenhagen in 1992 and 2015 respectively
#Find out what age most French people have in 2015