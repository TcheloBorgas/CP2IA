import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi

st.title("Previsão de Risco de Inadimplência e Análise de Clientes")

# Entrada de dados do cliente
margemBrutaAcumulada = st.number_input('Margem Bruta Acumulada', value=0.0)
faturamentoBruto = st.number_input('Faturamento Bruto', value=0)
percentualRisco = st.number_input('Percentual de Risco', value=0.0)

# Dados simulados para gráficos
dados_clientes = pd.DataFrame({
    'margemBrutaAcumulada': [0.3, 0.1, 0.05, 0.2, 0.15, 0.4],
    'faturamentoBruto': [500000, 200000, 100000, 300000, 250000, 450000],
    'percentualRisco': [0.1, 0.3, 0.6, 0.2, 0.5, 0.1],
    'risco_inadimplencia': [0, 0, 1, 0, 1, 0]
})

# Enviar dados para a API e obter a previsão
if st.button('Fazer Previsão'):
    dados_cliente = {
        'margemBrutaAcumulada': margemBrutaAcumulada,
        'faturamentoBruto': faturamentoBruto,
        'percentualRisco': percentualRisco
    }
    response = requests.post('http://127.0.0.1:5000/prever', json=dados_cliente)
    previsao = response.json()['previsao']
    previsao_texto = "Inadimplente" if previsao == 1 else "Bom Pagador"
    st.write(f'Previsão de Risco de Inadimplência: {previsao_texto}')
    
    # Adiciona o cliente atual aos dados simulados
    novo_cliente = pd.DataFrame([dados_cliente])
    novo_cliente['risco_inadimplencia'] = previsao
    dados_clientes = pd.concat([dados_clientes, novo_cliente], ignore_index=True)

    # Filtrar os dados para a comparação
    if previsao == 0:
        dados_comparacao = dados_clientes[dados_clientes['risco_inadimplencia'] == 0]
        comparacao_titulo = 'Bons Pagadores'
    else:
        dados_comparacao = dados_clientes[dados_clientes['risco_inadimplencia'] == 1]
        comparacao_titulo = 'Inadimplentes'

    # Plotar gráficos
    st.subheader('Gráficos de Análise de Clientes')

    fig, ax = plt.subplots(5, 1, figsize=(10, 30))

    # Gráfico 1: Comparação da margemBrutaAcumulada
    sns.boxplot(data=dados_comparacao, x='risco_inadimplencia', y='margemBrutaAcumulada', ax=ax[0])
    ax[0].set_title(f'Margem Bruta Acumulada - Comparação com {comparacao_titulo}')
    ax[0].scatter(previsao, margemBrutaAcumulada, color='red', s=100, zorder=10)

    # Gráfico 2: Histograma do Faturamento Bruto
    sns.histplot(dados_comparacao['faturamentoBruto'], bins=10, kde=True, ax=ax[1])
    ax[1].axvline(faturamentoBruto, color='red', linestyle='--')
    ax[1].set_title('Distribuição do Faturamento Bruto')

    # Gráfico 3: Histograma do Percentual de Risco
    sns.histplot(dados_comparacao['percentualRisco'], bins=10, kde=True, ax=ax[2])
    ax[2].axvline(percentualRisco, color='red', linestyle='--')
    ax[2].set_title('Distribuição do Percentual de Risco')

    # Gráfico 4: Scatter plot entre Margem Bruta Acumulada e Faturamento Bruto
    sns.scatterplot(data=dados_comparacao, x='margemBrutaAcumulada', y='faturamentoBruto', hue='risco_inadimplencia', ax=ax[3])
    ax[3].scatter(margemBrutaAcumulada, faturamentoBruto, color='red', s=100, zorder=10)
    ax[3].set_title('Margem Bruta Acumulada vs Faturamento Bruto')

    # Gráfico 5: Scatter plot entre Margem Bruta Acumulada e Percentual de Risco
    sns.scatterplot(data=dados_comparacao, x='margemBrutaAcumulada', y='percentualRisco', hue='risco_inadimplencia', ax=ax[4])
    ax[4].scatter(margemBrutaAcumulada, percentualRisco, color='red', s=100, zorder=10)
    ax[4].set_title('Margem Bruta Acumulada vs Percentual de Risco')

    st.pyplot(fig)

    st.write("### Explicações para Cada Gráfico")
    st.write("**Gráfico 1: Margem Bruta Acumulada**")
    st.write("Este gráfico mostra a Margem Bruta Acumulada do cliente em comparação com outros clientes da mesma categoria de risco (bons pagadores ou inadimplentes). "
             "Uma margem bruta acumulada maior geralmente indica um melhor desempenho financeiro.")
    st.write("**Gráfico 2: Histograma do Faturamento Bruto**")
    st.write("Este gráfico mostra a distribuição do Faturamento Bruto de outros clientes da mesma categoria de risco. "
             "A linha vermelha indica o faturamento bruto do cliente atual. "
             "Um faturamento maior pode indicar uma maior capacidade de pagamento.")
    st.write("**Gráfico 3: Histograma do Percentual de Risco**")
    st.write("Este gráfico mostra a distribuição do Percentual de Risco de outros clientes da mesma categoria de risco. "
             "A linha vermelha indica o percentual de risco do cliente atual. "
             "Um percentual de risco menor geralmente está associado a um menor risco de inadimplência.")
    st.write("**Gráfico 4: Margem Bruta Acumulada vs Faturamento Bruto**")
    st.write("Este gráfico mostra a relação entre a Margem Bruta Acumulada e o Faturamento Bruto. "
             "A posição do cliente é destacada em vermelho. Idealmente, um bom pagador deve ter tanto uma margem bruta acumulada "
             "quanto um faturamento bruto altos.")
    st.write("**Gráfico 5: Margem Bruta Acumulada vs Percentual de Risco**")
    st.write("Este gráfico mostra a relação entre a Margem Bruta Acumulada e o Percentual de Risco. "
             "A posição do cliente é destacada em vermelho. Um bom pagador tende a ter uma margem bruta acumulada alta e um percentual de risco baixo.")
