import streamlit as st

USUARIO = "ADMIN"
SENHA = "1234"

def tela_login():
    
    st.title("Tela do sistema")
    
    
    usuario = st.text_input("Login:")
    senha = st.text_input("Senha: ", type="password")



    if st.button("Entrar"):
        if usuario == USUARIO and senha == SENHA:

            st.session_state.logado = True
            st.rerun()
    
        else:
            st.error("Usuario ou senha invalidos!")
