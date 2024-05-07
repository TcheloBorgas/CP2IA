# orquestrador.py (Código Streamlit)
import streamlit as st
import requests
import pickle
import pandas as pd

def carregar_modelo_e_dados(modelo_caminho=r'C:\Users\pytho\Documents\GitHub\CP2IA\Model\modelo.pkl', dados_caminho='dados_teste.csv'):
    """
    Carrega o modelo e os dados de teste a partir dos caminhos fornecidos.

    Args:
    - modelo_caminho (str): Caminho para o arquivo do modelo serializado.
    - dados_caminho (str): Caminho para o arquivo de dados de teste (formato CSV).

    Retorna:
    - model (objeto): Modelo carregado.
    - X_test (DataFrame): Features de teste.
    - y_test (Series): Classes alvo de teste.
    - feature_names (list): Lista com os nomes das features.
    """
    # Carregar o modelo
    try:
        with open(modelo_caminho, 'rb') as f:
            model = pickle.load(f)
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return None, None, None, None

    # Carregar os dados de teste
    try:
        dados = pd.read_csv(dados_caminho)
    except Exception as e:
        print(f"Erro ao carregar os dados de teste: {e}")
        return None, None, None, None

    # Suponha que a última coluna seja a classe alvo
    feature_names = dados.columns[:-1]
    X_test = dados[feature_names]
    y_test = dados[dados.columns[-1]]

    return model, X_test, y_test, list(feature_names)



# Configurações iniciais da API
API_URL = "http://localhost:5000"




# Suponha que você tenha uma função para carregar seu modelo e dados de teste
model, X_test, y_test, feature_names = carregar_modelo_e_dados(model, )  # Defina esta função

# Botão para gerar gráficos de diagnóstico
if st.button('Gerar Diagnósticos do Modelo'):
    st.pyplot(plot_matriz_confusao(model, X_test, y_test))
    st.pyplot(plot_curva_roc(model, X_test, y_test))
    st.pyplot(plot_importancia_das_variaveis(model, feature_names))

# Selecione uma variável para mostrar distribuição
variavel_selecionada = st.selectbox('Escolha uma Variável', feature_names)
if variavel_selecionada:
    st.pyplot(plot_distribuicoes_das_variaveis(pd.DataFrame(X_test, columns=feature_names), variavel_selecionada, 'Classe'))



def send_prediction_request(data):
    """Envia uma solicitação de predição para a API e retorna a resposta."""
    response = requests.post(f"{API_URL}/predict", json=data)
    return response.json()

# Título da Aplicação
st.title('API de Modelo de Predição')

# Entradas para predição
st.header('Enviar dados para predição')
margem_bruta = st.text_input('Margem Bruta Acumulada', '0.3')
faturamento_bruto = st.text_input('Faturamento Bruto', '500000')
percentual_risco = st.text_input('Percentual de Risco', '0.1')

# Botão para enviar predição
if st.button('Fazer Predição'):
    prediction_data = {
        "margemBrutaAcumulada": float(margem_bruta),
        "faturamentoBruto": float(faturamento_bruto),
        "percentualRisco": float(percentual_risco)
    }
    result = send_prediction_request(prediction_data)
    st.write('Resultado da Predição:', result)
