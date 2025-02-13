import pandas as pd

# Dados atualizados das escolas municipais
data_escolas = {
    "Ano": [2019, 2020, 2021, 2022, 2023],
    "Escolas Municipais": [636, 632, 628, 620, 613]
}

# Dados das ofertas de matrículas
data_matriculas = {
    "Ano": [2019, 2020, 2021, 2022, 2023],
    "Matrículas": [58027, 57261, 55083, 39238, 37048]
}

# Criar DataFrames
df_escolas = pd.DataFrame(data_escolas)
df_matriculas = pd.DataFrame(data_matriculas)

# Salvar os DataFrames em arquivos Parquet
df_escolas.to_parquet("escolas.parquet")
df_matriculas.to_parquet("matriculas.parquet")