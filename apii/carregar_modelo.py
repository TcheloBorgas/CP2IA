import pickle
import streamlit as st

def carregar_modelo(caminho='data/modelo_melhor_salvo.pkl'):
    """
    Carrega um modelo de machine learning de um arquivo especificado.
    Retorna o modelo ou None em caso de erro.
    """
    try:
        with open(caminho, 'rb') as f:
            modelo = pickle.load(f)
        return modelo
    except Exception as e:
        st.error(f"Erro ao carregar o modelo: {e}")
        return None
