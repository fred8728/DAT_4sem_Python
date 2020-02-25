import numpy as np

#load the csv file: befkbhalderstatkode.csv into a numpy ndarray
filename = './befkbhalderstatkode.csv'
data = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

#3 Find out how many people lived in each of the 11 areas in 2015
def no_people_neighbourhood(n, mask):
    all_people_neighbourhood = data[mask & (data[:,1] == n)]
    sum_people = all_people_neighbourhood[:,4].sum() # index 4 is no of 'PERSONER'
    return sum_people

mask = (data[:,0] == 2015) 

amount_of_people = np.array([no_people_neighbourhood(n,mask) for n in neighb.keys()])
sort = amount_of_people.sort()
print('Amount of people in neighbourhoods:', amount_of_people)


#4 Make a bar plot to show the size of each city area from the smallest to the largest
import matplotlib.pyplot as plt
plt.figure()
plt.bar(list(neighb.values()), amount_of_people)
plt.title('Amount of people in neighbourhood')
plt.ylabel('Amount')
plt.xlabel('Neighbourhood')
plt.show()

#5 Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015

mask1 = (data[:,0] == 2015) & (data[:,2] > 65)
amount_above_65 = np.array([no_people_neighbourhood(n,mask1) for n in neighb.keys()])

print('People above 65 living in CPH 2015:', amount_above_65)

#6How many of those were from the other nordic countries (not dk)
statscodes = [5104,5106,5110,5120] #finland, island, norge, sverige
mask3 = (data[:,0] == 2015) & (data[:,2] > 65) & (np.in1d(data[:,3], statscodes)) #in1d test wheather each element of a 1-D array is also present in a second array (data[:,3], statscodes)
amount_nordic = np.array([no_people_neighbourhood(n,mask3) for n in neighb.keys()])
print('Nordic people above 65 living in CPH 2015:', amount_nordic)

#7 Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015
vesterbro = (data[:,0] >= 1992) & (data[:,1] == 4) 
oesterbro = (data[:,0] >= 1992) & (data[:,1] == 2) 
