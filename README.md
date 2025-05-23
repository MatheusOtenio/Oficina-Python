# Visualizador de Funções Matemáticas - Oficina Python

Aplicativo interativo desenvolvido em Python com Streamlit para visualização de funções matemáticas. Esta ferramenta didática permite aos estudantes explorar o comportamento de diferentes funções através da manipulação de parâmetros em tempo real.

## Índice

1. [Visão Geral](#visão-geral)
2. [Requisitos e Instalação](#requisitos-e-instalação)
3. [Como Executar](#como-executar)
4. [Funcionalidades](#funcionalidades)
5. [Estrutura do Código](#estrutura-do-código)
6. [Conceitos Matemáticos](#conceitos-matemáticos)
7. [Atividades Sugeridas](#atividades-sugeridas)
8. [Solução de Problemas](#solução-de-problemas)
9. [Recursos Adicionais](#recursos-adicionais)

## Visão Geral

O **Visualizador de Funções Matemáticas** permite a visualização interativa de três tipos de funções:

- **Funções Lineares**: `f(x) = ax + b`
- **Funções Quadráticas**: `f(x) = ax² + bx + c`
- **Funções Senoidais**: `f(x) = a * sin(bx)`

Esta aplicação foi desenvolvida como ferramenta de apoio ao ensino, permitindo que alunos visualizem graficamente o efeito da alteração de parâmetros nas funções.

## Requisitos e Instalação

### Requisitos
- Python 3.7 ou superior
- Bibliotecas: streamlit, numpy, matplotlib, pandas, pillow, altair, protobuf, pyarrow, pydeck, toml

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/visualizador-funcoes-matematicas.git
   cd visualizador-funcoes-matematicas
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar

1. Certifique-se de que o ambiente virtual está ativado (se estiver utilizando um)
2. Execute o comando:
   ```bash
   streamlit run main.py
   ```
3. O aplicativo será aberto automaticamente em seu navegador, geralmente no endereço `http://localhost:8501`

## Funcionalidades

### 1. Seleção de Função
Escolha entre funções lineares, quadráticas ou senoidais.

### 2. Configuração do Intervalo
Defina o intervalo de valores para o eixo x (mínimo e máximo).

### 3. Manipulação de Parâmetros
- **Linear**: Coeficientes angular (a) e linear (b)
- **Quadrática**: Coeficientes a, b e c
- **Senoidal**: Amplitude e frequência

### 4. Visualização Gráfica
Gráfico atualizado automaticamente com base nos parâmetros selecionados.

## Estrutura do Código

```python
# Importação de bibliotecas
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Interface e seleção de função
st.title("Visualizador de Funções Matemáticas")
funcao = st.selectbox("Escolha a função", ["Linear", "Quadrática", "Senoidal"])

# Definição do intervalo
x_min = st.slider("X mínimo", -10, 0, -5)
x_max = st.slider("X máximo", 0, 10, 5)
x = np.linspace(x_min, x_max, 400)

# Cálculo da função e plotagem
# [código específico para cada tipo de função]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(f"Gráfico da Função {funcao}")
ax.grid(True)
st.pyplot(fig)
```

## Conceitos Matemáticos

### Função Linear (`f(x) = ax + b`)
- `a`: coeficiente angular (inclinação da reta)
- `b`: coeficiente linear (valor de y quando x = 0)
- Se a > 0: reta crescente; a < 0: reta decrescente; a = 0: reta horizontal

### Função Quadrática (`f(x) = ax² + bx + c`)
- `a`: determina a abertura da parábola (a > 0: abre para cima; a < 0: abre para baixo)
- `b`: influencia na posição do vértice
- `c`: valor de y quando x = 0 (intercepto do eixo y)

### Função Senoidal (`f(x) = a * sin(bx)`)
- `a`: amplitude (altura máxima da onda)
- `b`: frequência (ciclos completos por unidade do eixo x)

## Atividades Sugeridas

### Para Funções Lineares
- Manipular valores de a e b para observar efeitos na inclinação e intercepto
- Encontrar valores para que a função cruze um ponto específico

### Para Funções Quadráticas
- Alterar o valor de a para observar mudanças na abertura da parábola
- Manipular valores para posicionar o vértice em coordenadas específicas
- Encontrar valores para que a parábola tenha raízes específicas

### Para Funções Senoidais
- Alterar amplitude e frequência para observar mudanças no formato da onda
- Ajustar a frequência para exibir um número específico de ciclos

## Solução de Problemas

- **Aplicativo não inicia**: Verifique dependências e versão do Python
- **Gráficos não aparecem**: Reinicie o aplicativo ou verifique erros no console
- **Valores não atualizam**: Reinicie o servidor ou limpe o cache do navegador

## Recursos Adicionais

### Documentação
- [Streamlit](https://docs.streamlit.io/)
- [NumPy](https://numpy.org/doc/)
- [Matplotlib](https://matplotlib.org/stable/contents.html)

### Referências Matemáticas
- [Khan Academy - Funções Lineares](https://pt.khanacademy.org/math/algebra/x2f8bb11595b61c86:functions/x2f8bb11595b61c86:intro-to-functions/a/evaluating-functions)
- [Khan Academy - Funções Quadráticas](https://pt.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratics)
- [Khan Academy - Funções Trigonométricas](https://pt.khanacademy.org/math/trigonometry/trig-function-graphs)
