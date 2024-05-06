from flask import jsonify, request
import pandas as pd

# Suponha que 'model' seja passado como argumento para a função
def predict(model):
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
