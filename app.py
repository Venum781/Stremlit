import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dados atualizados das escolas municipais
data = {
    "Ano": [2019, 2020, 2021, 2022, 2023],
    "Escolas Municipais": [636, 632, 628, 620, 613]  # Atualizado para 2019
}

# Criar DataFrame com os dados
df = pd.DataFrame(data)

# Calcular a taxa de crescimento/queda (variação percentual)
df["Variação (%)"] = df["Escolas Municipais"].pct_change() * 100
df["Variação (%)"] = df["Variação (%)"].fillna(0).round(2)  # Preencher NA com 0 e arredondar

# Função para exibir o gráfico principal
def plot_main_data(selected_data):
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(selected_data["Ano"], selected_data["Escolas Municipais"], color='skyblue', zorder=3)

    ax.set_xlabel("Ano", fontsize=14, labelpad=10)
    ax.set_ylabel("Número de Escolas Municipais", fontsize=14, labelpad=10)
    ax.set_title("Número de Escolas Municipais por Ano", fontsize=16, pad=20)

    ax.set_xticks(selected_data["Ano"])
    ax.set_xticklabels(selected_data["Ano"], fontsize=12)

    ax.grid(True, axis='y', linestyle='--', color='gray', alpha=0.5, zorder=2)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 5, f'{int(height)}', ha='center', va='bottom', fontsize=12)

    plt.subplots_adjust(top=0.85, bottom=0.15, left=0.1, right=0.95)
    st.pyplot(fig)

# Função para exibir o gráfico de taxa de variação
def plot_variation_data(selected_data):
    fig, ax = plt.subplots(figsize=(10, 6))
    line = ax.plot(
        selected_data["Ano"],
        selected_data["Variação (%)"],
        marker='o',
        color='green',
        label="Taxa de Queda",
        zorder=3
    )

    ax.set_xlabel("Ano", fontsize=14, labelpad=10)
    ax.set_ylabel("Taxa de Variação (%)", fontsize=14, labelpad=10)
    ax.set_title("Taxa de Queda no Número de Escolas Municipais", fontsize=16, pad=20)

    ax.set_xticks(selected_data["Ano"])
    ax.set_xticklabels(selected_data["Ano"], fontsize=12)
    ax.axhline(0, color='red', linestyle='--', linewidth=1.5, zorder=2)  # Linha de referência no eixo 0

    ax.grid(True, axis='y', linestyle='--', color='gray', alpha=0.5, zorder=1)

    # Ajuste para exibir valores percentuais e números inteiros das quedas
    for i, val in enumerate(selected_data["Variação (%)"]):
        y_pos = val  # Posição exatamente na taxa percentual
        ax.text(
            selected_data["Ano"][i],
            y_pos,
            f'{val}%',
            ha='center',
            fontsize=12,
            color='black'
        )
        if val < 0:  # Mostrar números inteiros apenas para quedas
            decrease = selected_data["Escolas Municipais"].iloc[i - 1] - selected_data["Escolas Municipais"].iloc[i]
            ax.text(
                selected_data["Ano"][i],
                y_pos - 1.5,  # Posição logo abaixo da taxa percentual
                f'{int(decrease)}',
                ha='center',
                fontsize=12,
                color='red'
            )

    plt.subplots_adjust(top=0.85, bottom=0.15, left=0.1, right=0.95)
    st.pyplot(fig)

# Título do aplicativo
st.title("Levantamento de Escolas Municipais em Salvador (2019-2023)")

# Descrição do app
st.markdown("""
Este aplicativo permite visualizar o número de escolas municipais de Salvador de 2019 a 2023. 
Além disso, é possível analisar a taxa de crescimento ou queda no número de escolas municipais ao longo dos anos.
""")

# Menu de seleção de gráfico
option = st.selectbox(
    "Escolha a visualização:",
    ["Número de Escolas Municipais", "Taxa de Queda", "Ambos os Gráficos"]
)

# Exibir os gráficos de acordo com a escolha do usuário
if option == "Número de Escolas Municipais":
    st.subheader("Gráfico do Número de Escolas Municipais")
    plot_main_data(df)

elif option == "Taxa de Queda":
    st.subheader("Gráfico da Taxa de Queda")
    plot_variation_data(df)

elif option == "Ambos os Gráficos":
    st.subheader("Gráfico do Número de Escolas Municipais")
    plot_main_data(df)
    st.subheader("Gráfico da Taxa de Queda")
    plot_variation_data(df)
