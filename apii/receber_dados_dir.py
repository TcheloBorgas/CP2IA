import streamlit as st

def receber_dados_usuario():
    """
    Recebe os dados de entrada do usuário via interface Streamlit.
    Retorna um dicionário contendo os dados fornecidos.
    """
    st.header("Insira os dados para previsão")
    margem_bruta = st.number_input('Margem Bruta Acumulada', format="%.2f", value=0.0)
    faturamento_bruto = st.number_input('Faturamento Bruto', format="%.2f", value=0.0)
    percentual_risco = st.number_input('Percentual de Risco', format="%.2f", value=0.0)

    dados = {
        'margemBrutaAcumulada': margem_bruta,
        'faturamentoBruto': faturamento_bruto,
        'percentualRisco': percentual_risco
    }
    return dados
