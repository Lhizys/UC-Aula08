import pandas as pd
import numpy as np


try: 
    ENDERECO_DADOS = 'tb_vendas2017_Miranda2.csv'

#venda de cada produto
    df_loja_miranda = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='utf-8')
    df_vendas_produtos = df_loja_miranda [['ID Produto', 'Quantidade Vendida']]
    print(df_vendas_produtos)
    print(30*"=")

#cadastro dos produtos
    ENDERECO_DADOS = 'tb_CadastroProdutos2017_Miranda.csv'
    df_loja_miranda = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='utf-8')
    df_cadastro_produtos = df_loja_miranda [['Categoria', 'Preco Unitario']]
    print(df_cadastro_produtos)
   



except ImportError as e:
    print(f'Erro: {e}')
    exit()