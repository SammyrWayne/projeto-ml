import streamlit as st
import csv
import os
import pandas as pd
from validate_docbr import CPF
from login import tela_login




if "logado" not in st.session_state:
    st.session_state.logado=False

if not st.session_state.logado:
    tela_login()

else:

validador_cpf = CPF()
print(validador_cpf.validate('123.456.789-00'))

# 🎨 Estilo fundo verde
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2e7d32;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Sistema de Lava Jato")

ARQUIVO = "clientes.csv"

#  Função para salvar cliente
def salvar_cliente(nome, cpf, endereco, dt_nasc, tp_cliente, sexo):
    arquivo_existe = os.path.isfile(ARQUIVO)

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)

        if not arquivo_existe:
            writer.writerow(["Nome", "CPF", "Endereco", "Nascimento", "Tipo", "Sexo"])

        # AGORA DENTRO DO WITH E COM LISTA
        writer.writerow([nome, cpf, endereco, dt_nasc, tp_cliente, sexo])

#  Função para carregar clientes
def carregar_clientes():
    if os.path.exists(ARQUIVO):
        return pd.read_csv(ARQUIVO)
    return pd.DataFrame()

#  Função para limpar dados
def limpar_clientes():
    if os.path.exists(ARQUIVO):
        os.remove(ARQUIVO)

# -------------------------
# Cadastro
# -------------------------
st.header("Cadastro de Clientes")

nome = st.text_input("Nome Completo")
cpf = st.text_input("CPF")
endereco = st.text_input("Endereço")
dt_nasc = st.date_input("Data de Nascimento")
tp_cliente = st.selectbox("Tipo de cliente", ["Pessoa Física", "Pessoa Jurídica"])
sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])

if st.button("Cadastrar"):
    if nome and endereco and cpf:
        if validador_cpf.validate(cpf):
            salvar_cliente(nome, cpf, endereco, dt_nasc, tp_cliente, sexo)
            st.success("✅ Cliente cadastrado com sucesso!")

        else:
            st.error("CPF Invalido!")
            
    else:
        st.error("⚠️ Preencha os dados obrigatórios!")

# -------------------------
# Busca
# -------------------------
st.header("Buscar Cliente")

busca = st.text_input("Digite o nome para buscar")
df = carregar_clientes()

if not df.empty:
    if busca:
        resultado = df[df["Nome"].str.contains(busca, case=False, na=False)]
        st.dataframe(resultado)
    else:
        st.dataframe(df)
else:
    st.info("Nenhum cliente cadastrado ainda!")

# -------------------------
# Limpar dados
# -------------------------
if st.button("Limpar dados dos clientes"):
    limpar_clientes()
    st.warning("Todos os dados foram apagados!")
