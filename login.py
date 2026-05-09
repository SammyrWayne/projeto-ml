import streamlit as st

USUARIO = "ADMIN"
SENHA = "1234"

def tela_login():
    
    
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1e1e1e;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    
    )

    st.title("Tela do sistema")
    
    usuario = st.text_input("Login:")
    senha = st.text_input("Senha: ", type="password")



if st.button("Entrar"):
    if usuario == USUARIO and senha == SENHA:

        st.session_state.logado = True
        st.rerun()
    
    else:
        st.error("Usuario ou senha invalidos!")