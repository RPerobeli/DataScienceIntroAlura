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
#indexação booleana
Dados[Dados > 100]
# %%
Dados[1] >= 10
# %%
