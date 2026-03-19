# 🧮 Explorador de Álgebra Linear com NumPy, Streamlit e Plotly

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-red?logo=streamlit&logoColor=white)](https://streamlit.io)
[![NumPy](https://img.shields.io/badge/NumPy-1.26%2B-blue?logo=numpy&logoColor=white)](https://numpy.org)
[![Plotly](https://img.shields.io/badge/Plotly-5.24%2B-blue?logo=plotly&logoColor=white)](https://plotly.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Aplicação **Streamlit** que oferece um ambiente interativo para explorar conceitos fundamentais de álgebra linear. O usuário pode editar matrizes e vetores diretamente na interface e visualizar os resultados em tempo real, com suporte a gráficos vetoriais 2D/3D gerados com Plotly.

---

## 1. 📌 Funcionalidades

1.1 **Sistemas Lineares**: Resolve sistemas `Ax = b` de dimensão configurável (2×2, 3×3, etc.), com exibição da solução.

1.2 **Autovalores e Autovetores**: Calcula autovalores e autovetores de matrizes quadradas, com visualização geométrica dos vetores no plano.

1.3 **Decomposições**: Implementa as decomposições QR e por valores singulares (SVD), exibindo as matrizes resultantes.

1.4 **Matrizes Especiais**: Gera matrizes de Vandermonde, identidade e diagonal a partir de parâmetros fornecidos pelo usuário.

1.5 **Produtos e Normas**: Calcula produto escalar, produto externo e norma euclidiana de vetores.

1.6 **Determinante e Inversa**: Calcula o determinante e, quando possível, a matriz inversa, com tratamento de matrizes singulares.

1.7 **Rank (Posto)**: Determina o número de linhas ou colunas linearmente independentes da matriz.

1.8 **Interface Interativa**: Todas as matrizes e vetores podem ser editados diretamente em tabelas dinâmicas, com atualização instantânea dos resultados.

1.9 **Visualizações Gráficas**: Plotagem de autovetores e representação visual de transformações lineares em 2D/3D.

---

## 2. 🏗️ Arquitetura do Sistema

A aplicação é dividida em módulos independentes, organizados para facilitar a manutenção e a adição de novas funcionalidades:

```
algebra-linear-matriz-3d/
├── app.py # Interface principal (Streamlit)
├── requirements.txt # Dependências do projeto
├── modules/ # Módulos de cálculo
│ ├── sistemas_linear.py
│ ├── autovalores.py
│ ├── decomposicoes.py
│ ├── matrizes_especiais.py
│ ├── produtos_normas.py
│ ├── determinante_inversa.py
│ └── rank.py
├── visualizacoes/ # Funções de plotagem
│ └── plot_autovetores.py
└── exemplos/ # Scripts de exemplo (opcional)
```


2.1 **Módulos de Cálculo**: Cada módulo encapsula uma família de operações (ex: `sistemas_linear.py` contém funções para resolver sistemas). Eles recebem os dados da interface e retornam os resultados de forma estruturada.

2.2 **Visualizações**: A pasta `visualizacoes/` contém funções que geram gráficos Plotly a partir dos dados calculados (ex: plotagem de autovetores).

2.3 **Interface (app.py)**: O arquivo principal orquestra a interação com o usuário, organiza as abas e chama os módulos apropriados.

---

## 3. 🚀 Como Executar o Projeto

### 3.1 Pré-requisitos

3.1.1 Python 3.10 ou superior instalado.
3.1.2 Git (opcional, para clonar o repositório).

### 3.2 Passo a Passo

3.2.1 **Clone o repositório** (ou baixe os arquivos)

   ```bash
   git clone https://github.com/Gussnogue/algebra-linear-matriz-3d.git
   cd algebra-linear-matriz-3d
   ```

3.2.2 **Crie e ative um ambiente virtual** (recomendado)

```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```
3.2.3 **Instale as dependências**

```
pip install -r requirements.txt
```

3.2.4 **Execute a aplicação**

```
streamlit run app.py
```

# 4. 🧠 Como Usar
4.1 Na barra lateral, selecione a operação desejada (ex: "Sistemas Lineares", "Autovalores", etc.).

4.2 Para operações que envolvem matrizes:

Edite os valores diretamente na tabela interativa.

Use os exemplos pré‑definidos (quando disponíveis) para testes rápidos.

4.3 Os resultados numéricos e gráficos são atualizados automaticamente após cada modificação.

4.4 Explore as visualizações em 2D/3D para compreender o significado geométrico das operações (ex: direção dos autovetores).

# 5. 📄 Licença
Este projeto está licenciado sob a MIT License. Sinta‑se à vontade para usar, modificar e distribuir.

# 6. 🤝 Contribuições
Contribuições são bem‑vindas! Se você tiver sugestões de novas funcionalidades ou melhorias:

Abra uma issue descrevendo a sugestão.

Envie um pull request com a implementação.
