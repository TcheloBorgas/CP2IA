import pandas as pd
import plotly.express as px
import streamlit as st

def plotar_comparacao(model, dados_usuario, caminho_dados_treinamento=r'C:\Users\pytho\Documents\GitHub\CP2IA\data\solicitacoescredito_clean.xlsx'):
    """
    Plota um gráfico de dispersão comparando os dados do usuário com os dados de treinamento.
    """
    try:
        # Carregar os dados de treinamento
        dados_treinamento = pd.read_csv(caminho_dados_treinamento)
        
        # Plotar gráfico de dispersão comparando os dados do usuário com os dados de treinamento
        fig = px.scatter(dados_treinamento, x="faturamentoBruto", y="margemBrutaAcumulada",
                         size="percentualRisco", color="Classe",
                         hover_name="Classe", log_x=True, size_max=60)
        
        # Adicionar os dados do usuário
        dados_usuario_df = pd.DataFrame([dados_usuario])
        dados_usuario_df['Classe'] = 'Usuário'
        fig.add_trace(px.scatter(dados_usuario_df, x="faturamentoBruto", y="margemBrutaAcumulada",
                                 size="percentualRisco", color="Classe").data[0])
        
        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Erro ao carregar ou plotar os dados: {e}")
