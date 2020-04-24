#!/usr/bin/env python
# coding: utf-8

# # Desafios da Aula 01

# In[1]:


# Importando as bilbiotecas
import pandas as pd

# Baixando o dataset "movies.csv" e armazenado em uma DataFrame
filmes = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/movies.csv')

# Trocando os nomes das colunas
filmes.columns = ['filmeId', 'titulo', 'generos']

# Visualizando o DataFrame
filmes.head()


# In[2]:


# Baixando o dataset "ratings.csv" e armazenado em uma DataFrame
avaliacoes = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/ratings.csv')

# Trocando os nomes das colunas
avaliacoes.columns = ['usuarioId', 'filmeId', 'nota', 'momento']

# Visualizando o DataFrame
avaliacoes.head()


# # Desafio 1
# Determine quantos filmes não obtiveram nota. Moetre quais são esses filmes.

# In[3]:


# Calculando as médias das notas por filme
notas_medias_por_filme = avaliacoes.groupby('filmeId')['nota'].mean()

# Juntando os DataFrames "filmes_com_medias" e "filmes"
medias_filmes = filmes.join(notas_medias_por_filme, on='filmeId')

# Separando os filmes sem nota
filmes_sem_notas = medias_filmes[medias_filmes['nota'].isna()]

# Calculando o total de filmes sem notas
total = filmes_sem_notas['titulo'].count()

# Mostrando o total de filmes sem notas e o títulos de todos eles
print(f'Total de filmes sem notas: {total}\n')
print('Lista de filmes sem notas')
for titulo in filmes_sem_notas['titulo']:
    print(f'==> {titulo}')


# # Desafio 2
# Junte os DataFrames **filmes** e **filmes_com_medias** e renomeie a columna ***nota*** para ***nota_media***

# In[4]:


# Renomeando a coluna "nota" para "nota_media"
medias_filmes = medias_filmes.rename(columns={'nota': 'nota_media'})

# Mostrando o DataFrame atualizado
medias_filmes.head()


# # Desafio 3
# Colocar o número de avaliações por filme, isto é, não só a média, mas também o TOTAL de votos por filme

# In[5]:


# Calculando o total de votos por filme
total_votos_por_filme = avaliacoes.groupby('filmeId')['nota'].count()

# Juntando os DataFrames "filmes_com_medias" e "total_votos_por_filme"
medias_filmes = medias_filmes.join(total_votos_por_filme, on='filmeId')

# Renomeando a coluna "nota" para "total_votos"
medias_filmes = medias_filmes.rename(columns={'nota': 'total_votos'})

# Mostrando o DataFrame atualizado
medias_filmes.head()


# # Desafio 4
# Arredonde as médias da coluna "nota_media" para duas casas decimais

# In[6]:


# Arredondando para duas casas decimais as médias da coluna "nota_media"
medias_filmes['nota_media'] = medias_filmes['nota_media'].round(2)

# Mostrando o DataFrame atualizado
medias_filmes.head()


# # Desafio extra
# Qual filme teve a maior quantidade de votos?

# In[7]:


# Criando uma "boolean mask"
selecao = medias_filmes['total_votos'] == medias_filmes['total_votos'].max()

# Encontrando o filme mais votado
mais_votado = medias_filmes[selecao]['titulo'].values[0]

# Mostrando o filme mais votado
print(f'O filme mais votado ==> {mais_votado}')


# # Desafio 5 e 6
# Descobrir quias são os gêneros dos filmes e quantos são os filmes de cada gênero.

# In[8]:


# Calculando o total de filmes por de gêneros
generos = pd.Series(medias_filmes.generos.str.get_dummies().sum().sort_values(ascending=False))

# Mostrando a quantidade de filmes por gênero
generos


# # Desafio 7
# Plotar o gráfico de aparições por gênero. Pode ser um gráfico de tipo = barra

# In[9]:


# Importando as bibliotecas necessárias
import matplotlib.pyplot as plt
import seaborn as sns

# Setando estilos
sns.set_style('whitegrid')
cmap = sns.diverging_palette(150, 275, l=55, s=80, n=9, center='dark', as_cmap=True)

# Tamanho da figura
plt.figure(figsize=(15, 8))

# Escolhendo o tipo de gráfico
generos.plot(kind='bar', colormap=cmap)

# Definindo o título
plt.title('Ocorrência de gêneros', fontsize=20)

# Definindo o eixo horizontal
plt.xlabel("Gêneros", fontsize=16)

# Definindo o eixo vertical
plt.ylabel("Ocorrência", fontsize=16)

# Rotacionando os gêneros em 45°
plt.xticks(rotation=45)

# Plotando a figura
plt.show()


# ### Ou usando o bilioteca seaborn

# In[10]:


# Setando o estilo
sns.set_style('whitegrid')

# Tamanho da segunda figura
plt.figure(figsize=(15, 8))

# Plotando o gráfico de barra com a seaborn
sns.barplot(x=generos.index, y=generos.values, 
            palette=sns.color_palette('cubehelix', n_colors=len(generos)+10))

# Definindo o título
plt.title('Ocorrência de gêneros', fontsize=20)

# Definindo o eixo horizontal
plt.xlabel("Gêneros", fontsize=16)

# Definindo o eixo vertical
plt.ylabel("Ocorrência", fontsize=16)

# Rotacionando os gêneros em 45°
plt.xticks(rotation=45)

plt.show()

