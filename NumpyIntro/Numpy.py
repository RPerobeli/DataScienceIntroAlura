# %%
import numpy as np
# main
# %%
np.arange(10)
# %%
# Criar arrays numpy
kmList = np.loadtxt('data/carros-km.txt')
kmList = kmList.astype(int)
kmList
# %%
Anos = np.loadtxt('data/carros-anos.txt')
Anos
# %%
Idade = 2019 - Anos
Idade
# %%
KmMedio = kmList/Idade
KmMedio
# %%
Dados = np.array([kmList, Idade])
Dados.shape
# %%
# indexação booleana
Dados[Dados > 100]
# %%
Dados[1] >= 10
# %%
Valor = np.loadtxt('data/carros-valor.txt')
Valor
# %%
dataset = np.column_stack((Anos, kmList, Valor))
# %%
np.mean(dataset[:, 1])
# %%
np.std(dataset[:, 1])
# %%
dataset[1].sum()
# %%
