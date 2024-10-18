import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

# Numpy : Créer un tableau
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)  # Multiplie chaque élément par 2

# Niveau avancé
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])

# Broadcasting : ajouter arr2 à chaque ligne de arr1
result = arr1 + arr2
print(result)

# Pandas : Créer un DataFrame
data = {'Nom': ['Alice', 'Bob', 'Charles'], 'Âge': [25, 30, 22]}
df = pd.DataFrame(data)
print(df)

# Niv avancé
# Créer un DataFrame de données de ventes
data = {
    'Produit': ['A', 'A', 'B', 'B', 'C'],
    'Ventes': [100, 200, 150, 50, 300],
    'Région': ['Est', 'Ouest', 'Est', 'Ouest', 'Est']
}
df = pd.DataFrame(data)

# Regrouper les ventes par produit
ventes_par_produit = df.groupby('Produit')['Ventes'].sum()
print(ventes_par_produit)
# Matplot : Créer un graphique simple
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphique simple')
plt.show()

# Niv avancé
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Créer deux graphiques côte à côte
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].plot(x, y1, label='sin(x)', color='blue')
ax[0].set_title('Sinus')
ax[0].set_xlabel('x')
ax[0].set_ylabel('sin(x)')
ax[0].legend()

ax[1].plot(x, y2, label='cos(x)', color='red')
ax[1].set_title('Cosinus')
ax[1].set_xlabel('x')
ax[1].set_ylabel('cos(x)')
ax[1].legend()

plt.show()
