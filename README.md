# Groq Chat Streamlit App

![robotzia](images/robotzia.webp)

Este aplicativo [Streamlit](https://streamlit.io/) integra-se com a [Groq API](https://groq.com/) para fornecer uma interface de chat onde os usuários podem interagir com modelos de linguagem avançados. Ele permite que os usuários escolham entre dois modelos para gerar respostas, melhorando a flexibilidade e a experiência do usuário no chat.

## Funcionalidades

- **Escolha de Modelos**: Selecione entre diferentes modelos de linguagem para se adaptar às suas necessidades.
- **Interface de Chat**: Uma interface de usuário limpa e intuitiva para uma interação suave.
- **Histórico de Conversas**: Visualize as interações passadas para referência futura.
- **Personalização**: Ajuste as configurações do modelo para otimizar a experiência de chat.

- Streamlit
- Groq Python SDK
- Python 3.7+

## Setup and Installation

- **Install Dependencies**:

  ```bash
  pip install streamlit groq
  ```
  - **Set Up Groq API Key**:

  Ensure you have an API key from Groq. This key should be stored securely using Streamlit's secrets management:

  ```toml
  # .streamlit/secrets.toml
  GROQ_API_KEY="your_api_key_here"
  ```
2. Navegue até o diretório do projeto:

    ```bash
    cd groq-streamlit
    ```
4. Execute o aplicativo:

    ```bash
    streamlit run streamlit_app.py
    ```
    
## Configuração

Certifique-se de configurar suas credenciais da API Groq no arquivo `.env`:

```env
GROQ_API_KEY=your_api_key_here
GROQ_API_URL=
```

## Uso
Após a instalação e configuração, você pode acessar o aplicativo via `http://localhost:8501` em seu navegador. Escolha o modelo desejado, insira sua mensagem e interaja com o modelo diretamente pelo chat.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para questões e sugestões, entre em contato pelo e-mail: contato@groq.com
