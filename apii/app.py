from carregar_modelo import carregar_modelo
from receber_dados_dir import receber_dados_usuario
from fazer_previsao import fazer_previsao
from plotagem import plotar_comparacao
import streamlit as st

def main():
    st.title("Dashboard de Previsão")
    
    model = carregar_modelo(r'C:\Users\pytho\Documents\GitHub\CP2IA\Model\modelo.pkl')
    dados_usuario = receber_dados_usuario()

    if st.button("Fazer Previsão"):
        predicao = fazer_previsao(model, dados_usuario)
        st.write(f"Previsão: {'Classe X' if predicao == 1 else 'Classe Y'}")
        plotar_comparacao(model, dados_usuario)

if __name__ == "__main__":
    main()
