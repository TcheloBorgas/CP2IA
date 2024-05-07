import pandas as pd
import streamlit as st

def fazer_previsao(model, dados):
    """
    Recebe um modelo e um dicionário com os dados de entrada do usuário,
    converte os dados para DataFrame e faz a previsão com o modelo.
    Retorna a previsão feita pelo modelo, ou uma mensagem de erro se algo der errado.
    """
    # Verifica se o modelo está carregado
    if model is None:
        st.error("Modelo não está carregado. Por favor, carregue o modelo antes de tentar fazer uma previsão.")
        return None

    # Verifica se os dados foram fornecidos
    if dados is None or not dados:
        st.error("Dados de entrada não fornecidos. Por favor, insira os dados necessários.")
        return None

    try:
        # Prepara os dados para a previsão
        df = pd.DataFrame([dados])  # Converte dicionário para DataFrame
        predicao = model.predict(df)  # Usa o modelo para fazer a previsão
        return predicao[0]  # Retorna o resultado da previsão
    except Exception as e:
        st.error(f"Erro ao fazer a previsão: {e}")
        return None
