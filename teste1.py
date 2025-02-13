import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Criar DataFrame com os dados
df_escolas = pd.DataFrame(data_escolas)
df_matriculas = pd.DataFrame(data_matriculas)

# Calcular a taxa de crescimento/queda (variação percentual)
df_escolas["Variação (%)"] = df_escolas["Escolas Municipais"].pct_change() * 100
df_escolas["Variação (%)"] = df_escolas["Variação (%)"].fillna(0).round(2)  # Preencher NA com 0 e arredondar

# Calcular a diferença no número de escolas fechadas a cada ano
df_escolas["Fechadas"] = df_escolas["Escolas Municipais"].diff().fillna(0).astype(int)
df_escolas["Fechadas"] = df_escolas["Fechadas"].abs()  # Considerar valor absoluto

# Calcular o total de escolas fechadas no período
total_fechadas = df_escolas["Fechadas"].sum()

def plot_common_style(ax):
    """Aplicar estilo comum aos gráficos."""
    ax.grid(True, axis='y', linestyle='--', color='gray', alpha=0.5, zorder=2)
    ax.set_xticks(df_escolas["Ano"])
    ax.set_xticklabels(df_escolas["Ano"], fontsize=12)
    plt.subplots_adjust(top=0.85, bottom=0.15, left=0.1, right=0.95)

def plot_main_data(selected_data):
    """Exibir o gráfico principal."""
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(selected_data["Ano"], selected_data["Escolas Municipais"], color='skyblue', zorder=3)

    ax.set_xlabel("Ano", fontsize=14, labelpad=10)
    ax.set_ylabel("Número de Escolas Municipais", fontsize=14, labelpad=10)
    ax.set_title("Número de Escolas Municipais por Ano", fontsize=16, pad=20)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 5, f'{int(height)}', ha='center', va='bottom', fontsize=12)

    plot_common_style(ax)
    st.pyplot(fig)

def plot_variation_data(selected_data):
    """Exibir o gráfico de taxa de variação com valores sobrepostos."""
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Gráfico de variação percentual
    ax1.plot(selected_data["Ano"], selected_data["Variação (%)"], marker='o', color='green', label="Taxa de Queda", zorder=3)
    ax1.set_xlabel("Ano", fontsize=14, labelpad=10)
    ax1.set_ylabel("Taxa de Variação (%)", fontsize=14, labelpad=10, color='green')
    ax1.axhline(0, color='red', linestyle='--', linewidth=1.5, zorder=2)
    
    for i, val in enumerate(selected_data["Variação (%)"]):
        y_pos = val
        if i > 0:  # Apenas para anos subsequentes a 2019
            ax1.text(selected_data["Ano"][i], y_pos, f'{val}%\n{int(selected_data["Escolas Municipais"].iloc[i - 1] - selected_data["Escolas Municipais"].iloc[i])}', 
                     ha='center', fontsize=12, color='red', linespacing=1.5)  # Sobrepor porcentagem e número inteiro em vermelho
        else:
            ax1.text(selected_data["Ano"][i], y_pos, f'{val}%', ha='center', fontsize=12, color='red')
    
    ax1.set_title("Taxa de Queda no Número de Escolas Municipais", fontsize=16, pad=20)
    plot_common_style(ax1)
    st.pyplot(fig)

def plot_enrollment_data(selected_data):
    """Exibir gráfico horizontal das ofertas de matrículas."""
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(selected_data["Ano"], selected_data["Matrículas"], color='coral', zorder=3)

    ax.set_ylabel("Ano", fontsize=14, labelpad=10)
    ax.set_xlabel("Número de Matrículas", fontsize=14, labelpad=10)
    ax.set_title("Ofertas de Matrículas por Ano", fontsize=16, pad=20)

    for bar in bars:
        width = bar.get_width()
        ax.text(width + 1000, bar.get_y() + bar.get_height() / 2, f'{int(width)}', ha='center', va='bottom', fontsize=12)

    ax.invert_yaxis()  # Inverter eixo Y para colocar os anos em ordem descendente
    plot_common_style(ax)
    st.pyplot(fig)

# Adicionar estilo CSS para aumentar ainda mais o tamanho da fonte no menu à esquerda
st.markdown("""
    <style>
    .css-1d391kg, .css-1v3fvcr {
        font-size: 25px;  /* Aumentar ainda mais o tamanho da fonte */
    }
    table {
        margin: auto;
        border-collapse: collapse;
    }
    th, td {
        padding: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Novo menu
st.sidebar.title("Menu")
menu_option = st.sidebar.selectbox(
    "Selecione a opção:",
    ["Escolas Municipais Fechadas", "Ofertas de Matrículas"]
)

# Texto abaixo do menu
st.sidebar.markdown("Este aplicativo tem como objetivo apresentar os dados de matrículas e o Número de Escolas Municipais fechadas em Salvador.")
st.sidebar.markdown("Todos os dados foram obtidos através do site do [Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)](https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar).")

if menu_option == "Escolas Municipais Fechadas":
    # Título do aplicativo
    st.title("Levantamento de Escolas Municipais em Salvador (2019-2023)")

    # Descrição do app
    st.markdown("""
    Este aplicativo permite visualizar o número de escolas municipais de Salvador de 2019 a 2023. 
    Além disso, é possível analisar a taxa de crescimento ou queda no número de escolas municipais ao longo dos anos.
    """)

    # Tabela de Fechadas Anual
    st.subheader("Número de Escolas Fechadas Anualmente")
    st.dataframe(df_escolas[["Ano", "Fechadas"]].applymap(lambda x: f'{x:.0f}'))

    # Mostrar o total de escolas fechadas
    st.subheader("Total de Escolas Fechadas")
    st.write(f"Total de escolas fechadas no período: {total_fechadas}")

    # Menu de seleção de gráfico
    option = st.selectbox("Escolha a visualização:", ["Número de Escolas Municipais", "Taxa de Queda", "Ambos os Gráficos"])

    # Exibir os gráficos de acordo com a escolha do usuário
    if option == "Número de Escolas Municipais":
        st.subheader("Gráfico do Número de Escolas Municipais")
        plot_main_data(df_escolas)
    elif option == "Taxa de Queda":
        st.subheader("Gráfico da Taxa de Queda")
        plot_variation_data(df_escolas)
    elif option == "Ambos os Gráficos":
        st.subheader("Gráfico do Número de Escolas Municipais")
        plot_main_data(df_escolas)
        st.subheader("Gráfico da Taxa de Queda")
        plot_variation_data(df_escolas)
elif menu_option == "Ofertas de Matrículas":
    st.title("Ofertas de Matrículas")
    st.markdown("Aqui você pode visualizar as ofertas de matrículas nas escolas municipais de Salvador de 2019 a 2023.")
    
    # Mostrar a tabela de matrículas
    st.subheader("Número de Matrículas Anualmente")
    st.dataframe(df_matriculas)

    # Gráfico horizontal das ofertas de matrículas
    st.subheader("Gráfico das Ofertas de Matrículas")
    plot_enrollment_data(df_matriculas)
