import matplotlib.pyplot as plt

people = {'Holger':25,'Helga':54,'Hasse':76,'Halvor':12,'Hassan':43,'Hulda':31,'Hansi':102}

plt.figure()
plt.bar(list(people.keys()), list(people.values()))

plt.title("People")
plt.xlabel("Name")
plt.ylabel("Age")

plt.show()