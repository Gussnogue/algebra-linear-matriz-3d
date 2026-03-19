import streamlit as st
import numpy as np
import plotly.graph_objects as go

from modules import (
    sistemas_linear, autovalores, decomposicoes,
    matrizes_especiais, produtos_normas, determinante_inversa, rank
)
from visualizacoes import plot_autovetores, plot_matriz

st.set_page_config(page_title="Álgebra Linear Interativa", layout="wide")
st.title("🧮 Explorador de Álgebra Linear com NumPy")
st.markdown("Selecione uma operação para visualizar e calcular.")

# Sidebar para escolha do módulo
opcao = st.sidebar.selectbox(
    "Escolha uma operação",
    [
        "Sistemas Lineares",
        "Autovalores e Autovetores",
        "Decomposições (QR, SVD)",
        "Matrizes Especiais",
        "Produtos e Normas",
        "Determinante e Inversa",
        "Rank"
    ]
)

if opcao == "Sistemas Lineares":
    st.header("📐 Sistemas Lineares")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("2x2")
        res2 = sistemas_linear.resolver_sistema_2x2()
        st.latex(res2["descricao"])
        st.write("Matriz A:")
        st.write(res2["A"])
        st.write("Vetor b:", res2["b"])
        st.success(f"Solução: x = {res2['solucao'][0]:.2f}, y = {res2['solucao'][1]:.2f}")
    with col2:
        st.subheader("3x3")
        res3 = sistemas_linear.resolver_sistema_3x3()
        st.latex(res3["descricao"])
        st.write("Matriz A:")
        st.write(res3["A"])
        st.write("Vetor b:", res3["b"])
        st.success(f"Solução: x = {res3['solucao'][0]:.2f}, y = {res3['solucao'][1]:.2f}, z = {res3['solucao'][2]:.2f}")

elif opcao == "Autovalores e Autovetores":
    st.header("🔢 Autovalores e Autovetores")
    res = autovalores.calcular_autovalores()
    st.write("Matriz A:")
    st.write(res["A"])
    st.write("Autovalores:", res["autovalores"])
    st.write("Autovetores (colunas):")
    st.write(res["autovetores"])
    fig = plot_autovetores.plot_autovetores(res["autovalores"], res["autovetores"])
    st.plotly_chart(fig, use_container_width=True)

elif opcao == "Decomposições (QR, SVD)":
    st.header("📦 Decomposições Matriciais")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("QR")
        res_qr = decomposicoes.decompor_qr()
        st.write("Matriz A:")
        st.write(res_qr["A"])
        st.write("Q:")
        st.write(res_qr["Q"])
        st.write("R:")
        st.write(res_qr["R"])
        st.write("Q @ R:")
        st.write(np.dot(res_qr["Q"], res_qr["R"]))
    with col2:
        st.subheader("SVD")
        res_svd = decomposicoes.decompor_svd()
        st.write("Matriz A:")
        st.write(res_svd["A"])
        st.write("U:")
        st.write(res_svd["U"])
        st.write("Valores singulares S:", res_svd["S"])
        st.write("Vt:")
        st.write(res_svd["Vt"])

elif opcao == "Matrizes Especiais":
    st.header("🔹 Matrizes Especiais")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Vandermonde")
        res_v = matrizes_especiais.vandermonde()
        st.write("x =", res_v["x"])
        st.write("Matriz:")
        st.write(res_v["V"])
    with col2:
        st.subheader("Identidade")
        res_i = matrizes_especiais.identidade()
        st.write(res_i["I"])
    with col3:
        st.subheader("Diagonal")
        res_d = matrizes_especiais.diagonal()
        st.write(res_d["d"])

elif opcao == "Produtos e Normas":
    st.header("⚡ Produtos e Normas")
    res = produtos_normas.calcular()
    st.write("Vetor a:", res["a"])
    st.write("Vetor b:", res["b"])
    st.write(f"Produto escalar: {res['dot']}")
    st.write(f"Norma de a: {res['norma_a']:.2f}")
    st.write(f"Norma de b: {res['norma_b']:.2f}")
    st.write("Produto externo:")
    st.write(res["outer"])

elif opcao == "Determinante e Inversa":
    st.header("📏 Determinante e Inversa")
    res = determinante_inversa.calcular()
    st.write("Matriz A:")
    st.write(res["A"])
    st.write(f"Determinante: {res['det']:.2f}")
    if res["inv"] is not None:
        st.write("Inversa:")
        st.write(res["inv"])
        st.write("A @ inv:")
        st.write(np.dot(res["A"], res["inv"]))
    else:
        st.warning("Matriz singular, não invertível.")

elif opcao == "Rank":
    st.header("📊 Rank (Posto)")
    res = rank.calcular()
    st.write("Matriz A:")
    st.write(res["A"])
    st.write(f"Rank: {res['rank']}")

st.sidebar.markdown("---")
st.sidebar.info("Este app usa NumPy e Plotly para demonstrar conceitos de álgebra linear.")

