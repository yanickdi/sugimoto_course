import matplotlib.pyplot as plt

def density_function(x):
    if x >= 3:
        return 0
    elif x >= 2:
        return 5/8
    elif x >= 1:
        return 1/4
    else:
        return x/4
        
y = []
x = []
for i in range(0, 5000):
    act_x = i / 1000
    x.append(act_x)
    y.append(density_function(act_x))

plt.plot(x, y)
plt.show()