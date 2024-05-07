import pandas as pd
import matplotlib.pyplot as plt

breadprice = pd.read_csv('breadprice.csv', index_col='Year')

breadprice_mean = breadprice.mean(axis=1)

plt.figure(figsize=(10, 6))
plt.plot(breadprice_mean.index, breadprice_mean.values, marker='o')
plt.title('Average Price of Bread per Year')
plt.xlabel('Year')
plt.ylabel('Average Price')

for x, y in zip(breadprice_mean.index, breadprice_mean.values):
    plt.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()
