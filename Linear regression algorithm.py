import numpy as np                                   #Importing All required Packages
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)
data = pd.read_csv(r"C:\Users\M V\Downloads\headbrain.csv")          #Reading the Headbrain dataset from local directory
print(data)
data.head(10)

x = data['Head Size(cm^3)'].values
y = data['Brain Weight(grams)'].values
plt.scatter(x, y, c='#ef5423', label='Scatter Plot')
plt.xlabel('Head Size(cm^3)')
plt.ylabel('Brain Weight(grams)')
plt.show()

x_mean = np.mean(x)
y_mean = np.mean(y)
print('X_mean ={} \n y_mean = {}'.format(x_mean, y_mean))

numberofdata = len(x)
num = 0
den = 0
for i in range(numberofdata):
    num += (x[i] - x_mean) * (y[i] - y_mean)
    den += (x[i] - x_mean) ** 2
M = num / den
print('M = ', M)

C = y_mean - (M * x_mean)
print("C = {}".format(C))
print('X_mean ={} \n y_mean = {}'.format(x_mean, y_mean))

maxx = np.max(x) + 100
maxy = np.max(y) - 100
linex = np.linspace(maxx, maxy, 1000)
liney = M * linex + C

plt.plot(linex, liney, c='#58b970', label='Regression line')
plt.scatter(x, y, c='#ef5423', label='Scatter Plot')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain weight in gms')
plt.show()

# r2square method to check

r2num = 0
r2den = 0

for j in range(numberofdata):
    yp = M * x[j] + C
    r2num += (yp - y_mean) ** 2
    r2den += (y[j] - y_mean) ** 2
r2 = r2num / r2den
print('\n \n R2 square method indicate the fit of a model')
print('r2 = ', 1 - r2)
