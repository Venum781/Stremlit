import streamlit as st
import pandas as pd

# Carregar o arquivo CSV
file_path = 'Tabela - Municipio com percentual de matriculas abaixo 80% (Escola).csv'
data = pd.read_csv(file_path)

# Selecionar as colunas relevantes
columns_to_display = [
    'Ordem',
    'Nome Escola',
    'Matrículas Educacenso  2023',
    'Matrículas Educacenso  2024',
    'Percentual de declaração (%)',
    'Diferença (2024-2023)'
]

# Configurar a página do Streamlit
st.title("Tabela de Matrículas por Escola")

# Adicionar informações adicionais
st.markdown("**UF:** Bahia")
st.markdown("**Município:** Salvador")

# Criar quadros com informações
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; text-align: center;">
        <strong>486.263</strong><br>
        Matrículas Educacenso (2024)<br>
        <strong>486.821</strong><br>
        Matrículas Educacenso (2023)<br>
        <strong>99,89%</strong><br>
        Percentual de declaração (%)
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; text-align: center;">
        <strong>1.572</strong><br>
        Nº de escolas fechadas<br>
        <strong>2.632</strong><br>
        Escolas Educacenso (2024)<br>
        <strong>59,73%</strong><br>
        Percentual de escolas fechadas (%)
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; text-align: center;">
        <strong>486.263</strong><br>
        Matrículas em escolas fechadas<br>
        <strong>486.263</strong><br>
        Matrículas Educacenso (2024)<br>
        <strong>100,00%</strong><br>
        Percentual de matrículas em escolas fechadas (%)
    </div>
    """, unsafe_allow_html=True)

# Exibir a tabela
st.dataframe(data[columns_to_display], width=1200, height=600)

# Adicionar a fonte dos dados
st.markdown("""
<div style="text-align: center; margin-top: 20px; font-style: italic;">
    Todos os dados foram obtidos através do site do Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).
</div>
""", unsafe_allow_html=True)
