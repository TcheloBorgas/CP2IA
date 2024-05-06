from flask import Flask, send_file, jsonify, request, render_template
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc
import numpy as np
import pandas as pd
import os
import joblib
import uuid
from predicao import predict as prediction_function
from graficos import plot_model_diagnostics
from flask_cors import CORS



app = Flask(__name__,template_folder=r'C:\Users\pytho\Documents\GitHub\CP2IA\template')
CORS(app)

# Carregar o modelo (ajuste o caminho conforme necessário)
model = joblib.load(r'C:\Users\pytho\Documents\GitHub\CP2IA\Model\modelo_melhor_salvo.pkl')


@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    return prediction_function(model)

@app.route('/generate_plots', methods=['POST'])
def generate_plots():
    data = request.get_json()
    X_test = pd.DataFrame(data['X_test'])
    y_test = pd.Series(data['y_test'])
    identifier = uuid.uuid4().hex  # Gera um identificador único para cada requisição

    # Gerar gráficos
    filenames = plot_model_diagnostics(model, X_test, y_test, identifier)
    return jsonify({'urls': [f'{request.host_url}{filename}' for filename in filenames]})

@app.route('/plots/<path:filename>')
def get_plot(filename):
    return send_file(filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
