import matplotlib.pyplot as plt

data = {'apple': 10,'banana':2,'citrus':32,'dragon fruit':8}

explode = (0, 0.1, 0, 0) 
fig1, ax1 = plt.subplots() 
ax1.pie(data.values(), labels=data.keys(), explode=explode, autopct=lambda p:'{:.2f}%({:.0f})'.format(p,(p/100)*sum(data.values())))

plt.show()