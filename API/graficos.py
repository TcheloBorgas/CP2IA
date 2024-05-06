import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc, accuracy_score
import numpy as np
import pandas as pd

def plot_model_diagnostics(model, X_test, y_test, identifier):
    """
    Gera gráficos para diagnóstico e salva como arquivos de imagem.
    """
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    filenames = []

    # Matriz de Confusão
    plt.figure()
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    confusion_filename = f'static/confusion_{identifier}.png'
    plt.savefig(confusion_filename)
    plt.close()
    filenames.append(confusion_filename)

    # Curva ROC
    plt.figure()
    fpr, tpr, thresholds = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f'ROC curve (area = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], linestyle='--')
    roc_filename = f'static/roc_{identifier}.png'
    plt.savefig(roc_filename)
    plt.close()
    filenames.append(roc_filename)

    return filenames