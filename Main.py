
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# main
notas = pd.read_csv("aula0/aula0/ml-latest-small/ratings.csv")
filmes = pd.read_csv("aula0/aula0/ml-latest-small/movies.csv")
# print(notas['rating'].unique())
# print(notas['rating'].value_counts())
# print(notas['rating'].mean())
# notas.rating.plot(kind='hist')
# print(notas.rating.describe())
# sns.boxplot(notas.rating)

# print(notas.query("movieId==1").rating.mean())
MediasPorFilme = notas.groupby('movieId').mean()["rating"]
print(MediasPorFilme)

# MediasPorFilme.plot(kind='hist')
plt.hist(MediasPorFilme)
plt.show()
