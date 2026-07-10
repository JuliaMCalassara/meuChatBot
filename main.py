# O que quero dentro do ChatBot
    # Titulo 
    # Campo de mensagem (input do chat)
    # A cada mensagem que o usuário enviar: 
        # mostrar a mensagem que o usuário enviou no chat 
        # pegar a pergunta e enviar para uma IA responder
        # exibir a resposta da IA na tela 

import streamlit as st
import google.generativeai as genai
import google.api_core.exceptions as exceptions

##genai.configure(api_key="AQ.Ab8RN6KcMHcANoErUSZSg7GZjRCqwfJ0RSyDLcUpSgguvp6c8Q")
##modelo = genai.GenerativeModel("gemini-1.5-flash-8b")

# IMPORTANTE: Substitua pela sua chave real ou use st.secrets para segurança
API_KEY = st.secrets["AQ.Ab8RN6KcMHcANoErUSZSg7GZjRCqwfJ0RSyDLcUpSgguvp6c8Q"]
genai.configure(api_key=API_KEY)

# CORREÇÃO: Atualizado de 'gemini-1.5-flash-8b' para 'gemini-2.5-flash'
modelo = genai.GenerativeModel("gemini-3.1-flash-lite")

##st.markdown("# :purple[ChatBot com IA]")## para deixar com cor, o comando é markdown
## ou esse comando..
st.markdown('<h1 style="color: #4B0082;">ChatBot com IA</h1>', unsafe_allow_html=True)

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message("user").write(texto_usuario) # user: ícone de usuário
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    # resposta IA
    # formato que a bibilioteca do google lê nativamente
    historico_gemini = [
        {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
        for m in st.session_state["lista_mensagens"]
    ]

    # gera a resposta enviando todo conteudo atualizado
    resposta_modelo = modelo.generate_content(historico_gemini)
    resposta_ia = resposta_modelo.text

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}

    st.session_state["lista_mensagens"].append(mensagem_ia)
# BLOCO DE PROTEÇÃO: Evita que o erro 429 trave o Streamlit
    try:
        resposta_modelo = modelo.generate_content(historico_gemini)
        resposta_ia = resposta_modelo.text

        st.chat_message("assistant").write(resposta_ia)
        mensagem_ia = {"role": "assistant", "content": resposta_ia}
        st.session_state["lista_mensagens"].append(mensagem_ia)
        
    except exceptions.ResourceExhausted:
        # Exibe mensagem amigável caso a cota do novo modelo também estoure
        st.error("⚠️ Cota da API esgotada! Aguarde alguns instantes ou verifique seus limites diários no Google AI Studio.")
        if st.session_state["lista_mensagens"]:
            st.session_state["lista_mensagens"].pop()