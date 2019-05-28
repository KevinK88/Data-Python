import matplotlib.pyplot as plt 
from random_walk import RandomWalk 

rw = RandomWalk(50000)
rw.fill_walk()
point_number = list(range(rw.num_points))
plt.scatter(rw.x_value,rw.y_value,c = point_number,cmap = plt.cm.Blues,edgecolor ='none',s=1)
# plt.scatter(0,0,c='green',edgecolor ='none',s=100)
# plt.scatter(rw.x_value[-1],rw.y_value[-1],c ='red', edgecolor ='none',s=100)
plt.show()

	