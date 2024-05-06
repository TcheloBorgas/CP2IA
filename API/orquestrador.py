import streamlit as st
import requests
import json

# Configurações iniciais da API
API_URL = "http://localhost:5000"  # Modifique conforme necessário para apontar para o seu servidor Flask

def send_prediction_request(data):
    """Envia uma solicitação de predição para a API e retorna a resposta."""
    response = requests.post(f"{API_URL}/predict", json=data)
    return response.json()

def send_generate_plots_request():
    """Envia uma solicitação para gerar gráficos e retorna as URLs dos gráficos."""
    response = requests.post(f"{API_URL}/generate_plots", json={})  # Adicione dados necessários para os gráficos
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

# Botão para gerar gráficos
st.header('Gerar Gráficos Diagnósticos')
if st.button('Gerar Gráficos'):
    plot_urls = send_generate_plots_request()
    if 'urls' in plot_urls:
        for url in plot_urls['urls']:
            st.image(url)

# Rodar a aplicação com `streamlit run app_streamlit.py` a partir do terminal
