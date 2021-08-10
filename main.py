import pandas as pd
import re
from sqlalchemy import create_engine
from helpers import Helpers

path = "files/base_teste.txt"
col_specs = [(0, 18), (19, 30), (31, 42), (43, 64), (65, 86), (87, 110), (111, 130), (131, 152)]
dataframe = pd.read_fwf(path, colspecs=col_specs)
dataframe_adjust = dataframe.rename(columns={'CPF': 'cpf', 'PRIVATE': 'private', 'INCOMPLETO': 'incompleto', 'DATA DA ÚLTIMA COMPRA': 'data_ultima_compra',
                                            'TICKET MÉDIO': 'ticket_medio', 'TICKET DA ÚLTIMA COMPRA': 'ticket_ultima_compra',
                                            'LOJA MAIS FREQUÊNTE': 'loja_mais_frequente', 'LOJA DA ÚLTIMA COMPRA': 'loja_ultima_compra'})


for cpf in dataframe_adjust.cpf:
    if Helpers.validar_cpf(cpf) is False:
        print('CPF inválido')

for cnpj in dataframe_adjust.loja_mais_frequente:
    if Helpers.validar_cnpj(cnpj) is False:
        print('CNPJ inválido')

for cnpj in dataframe_adjust.loja_ultima_compra:
    if Helpers.validar_cnpj(cnpj) is False:
        print('CNPJ inválido')

engine = create_engine(r"postgresql://postgres:supersenha@localhost/desafio_db")

c = engine.connect()
conn = c.connection

dataframe_adjust.to_sql("test_neoway", engine)

conn.close()
