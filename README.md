Nomes e Rms dos integrantes:

Marcelo Henrique - Rm: 98893
Daniel Alves de Souza - Rm: 552310
Matheus De CAstro Telles - Rm: 98413

# Análise e Tratamento de Dados de Solicitações de Crédito


## Este documento descreve as análises e o tratamento de dados realizados no notebook Model.ipynb, utilizando o conjunto de dados solicitacoescredito.csv, que contém informações sobre solicitações de crédito.

## Bibliotecas Utilizadas
Pandas: Para manipulação e análise de dados.
NumPy: Para suporte a grandes arrays e matrizes, junto com uma coleção de funções matemáticas para operar nesses arrays.
ydata_profiling: Para geração automática de relatórios de perfil dos dados, oferecendo uma visão detalhada dos dados, incluindo tipos, valores ausentes e estatísticas descritivas.


## Processo de Análise e Tratamento de Dados
Carregamento dos Dados

O conjunto de dados solicitacoescredito.csv é carregado para um DataFrame do pandas, fornecendo a base para as análises subsequentes.
Geração de Relatório de Perfil dos Dados

Utiliza-se o ProfileReport para gerar um relatório detalhado, que ajuda na identificação inicial de tipos de dados, valores ausentes e possíveis inconsistências.
Inspeção Inicial dos Dados

As primeiras 5 linhas do DataFrame são exibidas para uma inspeção visual rápida.
São apresentadas a forma do DataFrame, estatísticas descritivas e informações sobre os tipos de dados e valores ausentes, oferecendo uma compreensão inicial da estrutura e qualidade dos dados.
Tratamento de Valores Ausentes

É realizada uma análise para verificar a presença e o percentual de valores ausentes por coluna.
Definida a função valores_vazios, que trata valores ausentes em colunas categóricas, preenchendo-os com valores baseados na distribuição de frequência dos dados existentes. Para colunas numéricas, os valores ausentes são preenchidos com a mediana.

A função é aplicada a todas as colunas apropriadas do DataFrame, garantindo que nenhum valor ausente reste sem tratamento.
Verificação Final e Visualização dos Dados

Após o tratamento, é feita uma verificação final dos valores ausentes, confirmando a eficácia do processo de limpeza.
As primeiras 5 linhas do DataFrame tratado são exibidas para comparação com o estado inicial, demonstrando as mudanças resultantes do tratamento de dados.




