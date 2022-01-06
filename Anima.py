import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set()
path = r'C:\Users\HP\PycharmProjects\Operaciones_Calor\Data.xlsx'
df = pd.read_excel("Data.xlsx")
df2 = pd.read_excel("time.xlsx")
df3 = np.transpose(df)

ax = sns.heatmap(data=df3)
plt.show()