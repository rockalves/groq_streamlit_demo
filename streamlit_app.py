import streamlit as st
from typing import Generator
from groq import Groq

st.set_page_config(page_icon="🕵️‍♂️", layout="wide",
                   page_title="AndreIa - chat")


def icon(emoji: str):
    """AndreIa"""
    st.write(
        f'<span style="font-size: 30px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


icon("🕵️‍♂️")

st.subheader(":green[AndreIa] - Assistente I.A. do André", divider="green", anchor=False)
textArea='''
  **T A R E F A S ✔️**

  * [  ] Tarefa 1 - Texto descrevendo casos de uso de cada modelo  [U]
  * [  ] Tarefa 2 - componente copiar texto da última mensagem
  * [  ] Tarefa 2 - Dockerizar o app
  * [  ] Tarefa 3 - Especializar novos agentes (T.I, Saúde, Música, Cinema)
  * [  ] Tarefa 4 - 
  * [  ] Tarefa 5 - 
'''
st.markdown(textArea)

#########################
# To-do


#########################

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)

# Inicializa o histórico de acordo com o modelo selecionado. 
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None

# Define detalhes dos modelos
models = {
    "gemma-7b-it": {"name": "Gemma-7b-it", "tokens": 8192, "developer": "Google"},                          
    "gemma2-9b-it": {"name": "gemma2-9b-it", "tokens": 8192, "developer": "Google"}, #new
    "llama-3.1-70b-versatile": {"name": "llama-3.1-70b-versatile", "tokens": 8000, "developer": "Meta"}, #new
    # "llama2-70b-4096": {"name": "LLaMA2-70b-chat", "tokens": 4096, "developer": "Meta"},
    "llama3-70b-8192": {"name": "LLaMA3-70b-8192", "tokens": 8192, "developer": "Meta"},
    "llama3-8b-8192": {"name": "LLaMA3-8b-8192", "tokens": 8192, "developer": "Meta"},
    "mixtral-8x7b-32768": {"name": "Mixtral-8x7b-Instruct-v0.1", "tokens": 32768, "developer": "Mistral"},
}

# Layout para o modelo selecionado e o slider max_tokens
col1, col2 = st.columns(2)

with col1:
    model_option = st.selectbox(
        "Escolha um modelo, de acordo com sua necessidade:",
        options=list(models.keys()),
        format_func=lambda x: models[x]["name"],
        index=4  # Default : mixtral
    )

# Detecta o modelo modificado e limpa o histórico do chat ao modificar o modelo.
if st.session_state.selected_model != model_option:
    st.session_state.messages = []
    st.session_state.selected_model = model_option

max_tokens_range = models[model_option]["tokens"]

with col2:
    # Ajusta max_tokens slider dinamicamente, de acordo com o modelo selecionado
    max_tokens = st.slider(
        "Max Tokens:",
        min_value=512,  # Valor mínimo para ter alguma flexibilidade
        max_value=max_tokens_range,
        # Valor padrão ou o máximo de tokens do modelo se vazio.
        value=min(32768, max_tokens_range),
        step=512,
        help=f"Ajuste o número máximo de tokens (palavras) para a resposta do modelo. Máximo para o modelo selecionado: {max_tokens_range}"
    )

# Mostra as mensagens de chat do histórico ao subir a aplicação 
for message in st.session_state.messages:
    avatar = '🤖' if message["role"] == "assistant" else '👨‍💻'
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    """Gerar o conteúdo da resposta do chat a partir da resposta da API Groq."""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content


if prompt := st.chat_input("Digite seu prompt aqui..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user", avatar='👨‍💻'):
        st.markdown(prompt)

    # Fetch response from Groq API
    try:
        chat_completion = client.chat.completions.create(
            model=model_option,
            messages=[
                {
                    "role": m["role"],
                    "content": m["content"]
                }
                for m in st.session_state.messages
            ],
            max_tokens=max_tokens,
            stream=True
        )

        # Use the generator function with st.write_stream
        with st.chat_message("assistant", avatar="🤖"):
            chat_responses_generator = generate_chat_responses(chat_completion)
            full_response = st.write_stream(chat_responses_generator)
    except Exception as e:
        st.error(e, icon="🚨")

    # Append the full response to session_state.messages
    if isinstance(full_response, str):
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response})
    else:
        # Handle the case where full_response is not a string
        combined_response = "\n".join(str(item) for item in full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": combined_response})
