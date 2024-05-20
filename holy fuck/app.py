from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Carregar o modelo
modelo = joblib.load(r'Model\modelo.pkl')

@app.route('/prever', methods=['POST'])
def prever():
    dados_cliente = request.json
    df = pd.DataFrame([dados_cliente])
    previsao = modelo.predict(df)
    return jsonify({'previsao': int(previsao[0])})


if __name__ == '__main__':
    app.run(debug=True)
