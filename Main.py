
from operator import index
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# main
notas = pd.read_csv("aula0/aula0/ml-latest-small/ratings.csv")
filmes = pd.read_csv("aula0/aula0/ml-latest-small/movies.csv")
tmbd = pd.read_csv("aula0/aula0/ml-latest-small/tmdb_5000_movies.csv")
'''
 print(notas['rating'].unique())
 print(notas['rating'].value_counts())
 print(notas['rating'].mean())
 notas.rating.plot(kind='hist')
 print(notas.rating.describe())
 sns.boxplot(notas.rating)

 print(notas.query("movieId==1").rating.mean())
 MediasPorFilme = notas.groupby('movieId').mean()["rating"]
 print(MediasPorFilme)

 MediasPorFilme.plot(kind='hist')
 plt.hist(MediasPorFilme)
 plt.show()

 print(tmbd.original_language.unique())
 '''


categorias_por_lingua = tmbd["original_language"].value_counts(
).to_frame().reset_index()
# print(categorias_por_lingua)
plt.pie(categorias_por_lingua["original_language"],
        labels=categorias_por_lingua["index"])
plt.show()

categorias_por_lingua = tmbd["original_language"].value_counts(
).to_frame()
total_geral = categorias_por_lingua["original_language"].sum()
total_ingles = categorias_por_lingua["original_language"].loc["en"]
total_resto = total_geral - total_ingles
dados = {
    "lingua": ["ingles", "outros"],
    "qtd": [total_ingles, total_resto]
}
dados = pd.DataFrame(dados)

plt.pie(dados["qtd"], labels=dados["lingua"])
plt.show()

categorias_por_lingua_outros = categorias_por_lingua.reset_index().query(
    "index != 'en'")

print(categorias_por_lingua_outros)
plt.pie(categorias_por_lingua_outros['original_language'],
        labels=categorias_por_lingua_outros['index'])
plt.show()


sns.barplot(x=categorias_por_lingua_outros['index'],
            y=categorias_por_lingua_outros['original_language'])
plt.show()
