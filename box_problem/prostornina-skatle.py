# odvisnost prostornine kvadraste škatle od dolžine in širine, pri konst tretji dimenziji
# a + b + c = 1.57

import math
import numpy as np
import matplotlib.pyplot as plt
import time

vsota_dolzin = 1.57
z_komp = 0.21
x_values = np.zeros(1)
y_values = np.zeros(1)
x = np.linspace(0, vsota_dolzin - z_komp, 100)
""" z = np.empty(1)
z.fill(z_komp) """

for x_i in x:
    y = np.linspace(0, vsota_dolzin - z_komp - x_i, 100)
    xek = np.empty(100)
    xek.fill(x_i)
    y_values = np.append(y_values, y)
    x_values = np.append(x_values, xek)


V = x_values*y_values*z_komp


print(x_values, len(x_values))
print(y_values, len(y_values))


fig = plt.figure()

ax = plt.axes(projection ='3d')
ax.scatter(x_values, y_values, V)
ax.set_title(r'$V (x, y)$' + ' za škatlo pri z=konst')
ax.set_xlabel("x " + r'$[m]$')
ax.set_ylabel("y " + r'$[m]$')
ax.set_zlabel("V " + r'$[m^3]$')
plt.show()