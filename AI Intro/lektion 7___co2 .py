#lektion 7

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from mpl_toolkits.mplot3d import Axes3D

co2 = pd.read_csv("CO2data.csv")

x = co2[['Weight', 'Volume']].values
y = co2['CO2'].values

# 3D SCATTER (original visualization)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[:, 0], x[:, 1], y, c='b', marker='o')
ax.set_xlabel('Weight')
ax.set_ylabel('Volume')
ax.set_zlabel('CO2')
ax.set_title("3D plot af data")
plt.show()

# -----------------------------------------------------
# LINEÆR REGRESSION
# -----------------------------------------------------

lin_reg_weight = LinearRegression()
lin_reg_volume = LinearRegression()
lin_reg_begge = LinearRegression()

x_weight = co2[['Weight']]
x_volume = co2[['Volume']]

lin_reg_weight.fit(x_weight, y)
lin_reg_volume.fit(x_volume, y)
lin_reg_begge.fit(x, y)

y_weight = lin_reg_weight.predict(x_weight)
y_volume = lin_reg_volume.predict(x_volume)
y_begge = lin_reg_begge.predict(x)

# -----------------------------------------------------
# MSE
# -----------------------------------------------------
mse_weight = mean_squared_error(y, y_weight)
mse_volume = mean_squared_error(y, y_volume)
mse_begge = mean_squared_error(y, y_begge)

print("MSE Weight:", mse_weight)
print("MSE Volume:", mse_volume)
print("MSE Begge:", mse_begge)

print(lin_reg_begge.predict([[2300, 1300]]))

# -----------------------------------------------------
# MSE BARPLOT
# -----------------------------------------------------
plt.figure(figsize=(6,4))
plt.bar(['Weight', 'Volume', 'Begge'], [mse_weight, mse_volume, mse_begge])
plt.title('MSE sammenligning')
plt.ylabel('MSE')
plt.xlabel('Model')
plt.show()
'''
# -----------------------------------------------------
# LINEÆR REGRESSION VISUALISERING - WEIGHT
# -----------------------------------------------------
plt.figure(figsize=(6,4))
plt.scatter(x_weight, y, label="Data")
plt.plot(x_weight, y_weight, label="Linær regression", linewidth=2)
plt.title("Lineær regression - Weight")
plt.xlabel("Weight")
plt.ylabel("CO2")
plt.legend()
plt.show()

# -----------------------------------------------------
# LINEÆR REGRESSION VISUALISERING - VOLUME
# -----------------------------------------------------
plt.figure(figsize=(6,4))
plt.scatter(x_volume, y, label="Data")
plt.plot(x_volume, y_volume, label="Linær regression", linewidth=2)
plt.title("Lineær regression - Volume")
plt.xlabel("Volume")
plt.ylabel("CO2")
plt.legend()
plt.show()

# -----------------------------------------------------
# 3D PLAN FOR BEGGE
# -----------------------------------------------------
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

# Scatter
ax.scatter(x[:,0], x[:,1], y, marker='o')

# Lav grid til regressionsplanen
x_surf = np.linspace(x[:,0].min(), x[:,0].max(), 20)
y_surf = np.linspace(x[:,1].min(), x[:,1].max(), 20)
x_surf, y_surf = np.meshgrid(x_surf, y_surf)
z_surf = (lin_reg_begge.intercept_
          + lin_reg_begge.coef_[0] * x_surf
          + lin_reg_begge.coef_[1] * y_surf)

# Tegn plane
ax.plot_surface(x_surf, y_surf, z_surf, alpha=0.5)

ax.set_xlabel('Weight')
ax.set_ylabel('Volume')
ax.set_zlabel('CO2')
ax.set_title("Lineær regression - Begge variabler (3D plan)")
plt.show()
'''

