import pandas as pd
cidades = pd.read_csv(r"C:\Users\doomw\OneDrive\Documentos\Projeto_california\california_cities.csv")
print(cidades.head())

latitude, longitude = cidades["latd"], cidades["longd"]
populacao, area = cidades["population_total"], cidades["area_total_km2"]

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
plt.scatter(longitude, latitude, label=None, c=np.log10(populacao),
            cmap='viridis', s=area, linewidth=0, alpha=0.5)
plt.gca().set_aspect('equal')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(label='log$_{10}$(populacão)')
plt.clim(3, 7)

for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area, label=str(area) + 'km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Áreas da cidade')
plt.title("Área e população das cidades da Califórnia")
plt.show()