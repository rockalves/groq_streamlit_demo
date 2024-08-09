# Groq Chat Streamlit App

![robotzia](images/robotzia.webp)

Este aplicativo [Streamlit](https://streamlit.io/) integra-se com a [Groq API](https://groq.com/) para fornecer uma interface de chat onde os usuários podem interagir com modelos de linguagem avançados. Ele permite que os usuários escolham entre dois modelos para gerar respostas, melhorando a flexibilidade e a experiência do usuário no chat.

## Funcionalidades

- **Escolha de Modelos**: Selecione entre diferentes modelos de linguagem para se adaptar às suas necessidades.
- **Interface de Chat**: Uma interface de usuário limpa e intuitiva para uma interação suave.
- **Histórico de Conversas**: Visualize as interações passadas para referência futura.
- **Personalização**: Ajuste as configurações do modelo para otimizar a experiência de chat.

## Requisitos

- Python 3.8 ou superior
- Conta na Groq API
- Dependências listadas no arquivo `requirements.txt`

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/groq-chat-app.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd groq-chat-app
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Execute o aplicativo:
    ```bash
    streamlit run app.py
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
