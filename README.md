# meuChatBot

Chatbot com IA desenvolvido em Python durante o curso Jornada Python, da Hashtag.
Usa a API do Google Gemini para responder às mensagens do usuário em uma
interface de chat criada com Streamlit.

## O que ele faz
- Exibe uma interface de chat com título e campo para digitar mensagens
- Mostra no chat cada mensagem enviada pelo usuário
- Envia a pergunta, junto com o histórico da conversa, para a IA (Gemini)
  e exibe a resposta na tela
- Mantém o histórico da conversa durante a sessão
- Mostra um aviso amigável quando a cota da API é esgotada, em vez de travar

## Tecnologias
- Python
- Streamlit
- Google Generative AI (Gemini API)

## Como rodar
1. Clone o repositório
2. Instale as dependências: `pip install streamlit google-generativeai`
3. Crie uma chave de API no Google AI Studio
4. Crie a pasta `.streamlit` com o arquivo `secrets.toml` contendo:
   `GEMINI_API_KEY = "sua_chave_aqui"`
5. Execute: `streamlit run main.py`

## O que eu adicionei
O projeto segue a estrutura do curso, com estas diferenças:
- Troquei a IA da OpenAI (GPT-4o) pela do Google (Gemini)
- Converti o histórico da conversa para o formato que o Gemini aceita
  (papel "model" e campo "parts")
- Guardei a chave da API em `st.secrets`, em vez de escrevê-la no código
- Adicionei tratamento do erro de cota esgotada da API, com mensagem de aviso
- Personalizei o título do chat com HTML e uma cor própria
