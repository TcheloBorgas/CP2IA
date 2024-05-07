from flask import Flask, jsonify, request
import pandas as pd
import pickle

# Inicializa o aplicativo Flask
app = Flask(__name__)




import pickle

try:
    with open(r'C:\Users\pytho\Documents\GitHub\CP2IA\Model\modelo.pkl', 'rb') as file:
        model = pickle.load(file)
    print(type(model))  # Isso mostrará o tipo do objeto carregado
    print(hasattr(model, 'predict'))  # Isso verificará se o objeto tem o método predict
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")






@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Modelo não carregado corretamente.'}), 500

    try:
        data = request.get_json()
        input_data = pd.DataFrame([data])
        colunas = ['margemBrutaAcumulada', 'faturamentoBruto', 'percentualRisco']
        if not all(column in input_data.columns for column in colunas):
            return jsonify({'error': 'JSON inválido, falta uma ou mais colunas necessárias.'}), 400
        prediction = model.predict(input_data)
        return jsonify({'Prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
