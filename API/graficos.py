import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc
import numpy as np
import pandas as pd

def plot_matriz_confusao(model, X_test, y_test):
    """Gera e retorna uma matriz de confusão"""
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Matriz de Confusão')
    plt.ylabel('Classe Real')
    plt.xlabel('Classe Prevista')
    plt.close()
    return plt

def plot_curva_roc(model, X_test, y_test):
    """Gera e retorna uma curva ROC"""
    y_proba = model.predict_proba(X_test)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(10, 7))
    plt.plot(fpr, tpr, label=f'Curva ROC (área = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], linestyle='--')
    plt.xlabel('Taxa de Falsos Positivos')
    plt.ylabel('Taxa de Verdadeiros Positivos')
    plt.title('Curva Característica Operacional do Receptor (ROC)')
    plt.legend(loc='lower right')
    plt.close()
    return plt

def plot_importancia_das_variaveis(model, nomes_das_variaveis):
    """Gera e retorna um gráfico de importância das variáveis"""
    importancias = model.feature_importances_
    indices = np.argsort(importancias)[::-1]
    plt.figure(figsize=(10, 7))
    plt.title('Importância das Variáveis')
    sns.barplot(y=[nomes_das_variaveis[i] for i in indices], x=importancias[indices], orient='h')
    plt.xlabel('Importância Relativa')
    plt.close()
    return plt

def plot_distribuicoes_das_variaveis(dados, nome_variavel, nome_classe):
    """Gera e retorna um gráfico de distribuição das variáveis por classe"""
    plt.figure(figsize=(10, 7))
    for valor_classe in dados[nome_classe].unique():
        sns.histplot(dados[dados[nome_classe] == valor_classe][nome_variavel], kde=True, label=f'Classe {valor_classe}')
    plt.title(f'Distribuição de {nome_variavel} por Classe Alvo')
    plt.ylabel('Densidade')
    plt.xlabel(nome_variavel)
    plt.legend()
    plt.close()
    return plt
