#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Para criar resultados exibidos na tela, porém estes possuem botões para interação com usuario.
import streamlit as st
import joblib

import warnings
warnings.filterwarnings('ignore')


# In[3]:


modelo = joblib.load('modelo.joblib')


# In[4]:


# Este é o print das colunas de 'base_teste.columns'

# SEPARAMOS ELAS EM Dicionarios com:

# Colunas com Caracteristicas numericas
x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_listings_count': 0}
# Com, Verdadeiro ou Falso
x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}


# Com Listas
x_listas = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancelation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
            }


dicionario = {}
# ESTE 'FOR' AS 3 CHAVES DO DICIONARIO 'x-listas' com cada um dos itens/valores da
#.. lista que compõem os valores destas. 
for item in x_listas:
    # Percorre os valores/Listas das chaves do Dicionario 'x_listas'
    for valor in x_listas[item]:
        # Recebe e concatena (com '_' ) as 3 chaves com cada um dos itens de suas Listas.
        dicionario[f'{item}_{valor}'] = 0

        

        

# Criando botões com campos numericos:
for item in x_numericos:
    # Criando botão com texto referente a cada um dos itens percorridos, Usando o 'Streamlit'
    valor = st.number_input(f'{item}')

# Boteos com valores binários (Yes or Not)
for item in x_tf:
    if valor == 'Sim':
        x_tf[item] = 1
    else:
        x_tf[item] = 0
            
            
    #valor = st.selectbox(f'{item}', ('Sim', 'Não'))

# Passando os valores das Chaves do Dicionario como botão de multiplas opções
for item in x_listas:
    valor = st.selectbox(f'{item}', x_listas[item]) # Mostra valor das chaves.  
    # Mesmo tratamento de atribuição binaria feito em 'dicionario'
    dicionario[f'{item}_{valor}'] = 1
    
    
botao = st.button("Prever Valores Dos Imóveis")


if botao:
    # Este metodo junta um dicionario no outro
    dicionario.update(x_numericos)
    dicionario.update(x_tf)
    # É necessário requisitar que o DataFrame seja criado com um Indice usando 'index=[0]'
    valores_x = pd.DataFrame(dicionario, index =[0])
    # Carrega o metodo estatistico escolhido/usado OU Modelo Usado e salvo no arquivo .joblib
    modelo = joblib.load('modelo.joblib')
    preco = modelo.predict(valores_x)
    #st.write(preco)
    st.write(preco[0])                         
                         


# ##### Para visuzalizar a numeração das linhas, tecle  'Ctrl-m t' e então digite 'L'

# In[ ]:


# Aqui vemos o resultado da combinação das 3 chaves(nomes delas) com seus valores
#..contidos nas listas pertencentes a cada um deles (Atribuimos 0 zeros)
for x, y in dicionario.items():
    print(f'{x}\t{y}', end='\n')
    #print(y)


# In[ ]:


for x, y in x_listas.items():
    print(f'{x}\t{y}', end='\n')


# In[ ]:




