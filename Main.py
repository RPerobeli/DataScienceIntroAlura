
import pandas as pd
import seaborn as sns

# main
notas = pd.read_csv("aula0/aula0/ml-latest-small/ratings.csv")
# print(notas['rating'].unique())
# print(notas['rating'].value_counts())
# print(notas['rating'].mean())
# notas.rating.plot(kind='hist')
print(notas.rating.describe())
# sns.boxplot(notas.rating)
