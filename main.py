import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Visualizador de Funções Matemáticas")

# Escolha da função
funcao = st.selectbox("Escolha a função", ["Linear", "Quadrática", "Senoidal"])

# Intervalo
x_min = st.slider("X mínimo", -10, 0, -5)
x_max = st.slider("X máximo", 0, 10, 5)
x = np.linspace(x_min, x_max, 400)

# Parâmetros
if funcao == "Linear":
    a = st.slider("Coeficiente angular (a)", -5.0, 5.0, 1.0)
    b = st.slider("Coeficiente linear (b)", -5.0, 5.0, 0.0)
    y = a * x + b

elif funcao == "Quadrática":
    a = st.slider("Coeficiente a", -2.0, 2.0, 1.0)
    b = st.slider("Coeficiente b", -5.0, 5.0, 0.0)
    c = st.slider("Coeficiente c", -5.0, 5.0, 0.0)
    y = a * x**2 + b * x + c

elif funcao == "Senoidal":
    amp = st.slider("Amplitude", 0.1, 5.0, 1.0)
    freq = st.slider("Frequência", 0.1, 5.0, 1.0)
    y = amp * np.sin(freq * x)

# Plotando
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(f"Gráfico da Função {funcao}")
ax.grid(True)
st.pyplot(fig)
