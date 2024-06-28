# Twitter Trends FastAPI Project

## Descrição

Este projeto é uma aplicação FastAPI que coleta e exibe tendências do Twitter. Utiliza MongoDB para armazenamento de dados e inclui um dashboard interativo desenvolvido com Streamlit para visualização das tendências. O projeto também permite a geração de relatórios em PDF das tendências coletadas.

## Estrutura do Projeto

```plaintext
DIO-DESAIO-TWITTER/
├── src/
│   ├── __init__.py
│   ├── connection.py
│   ├── constants.py
│   ├── responses.py
│   ├── secrets.py
│   ├── services.py
│   └── reports.py
├── teste/
│   └── test_service.py
├── main.py
├── docker-compose.yml
├── .editorconfig
├── setup.cfg
└── requirements.txt


Pré-requisitos
Docker
Docker Compose
Python 3.9+
Virtualenv (opcional, mas recomendado)
Configuração
Clone o repositório:
git clone https://github.com/seu-usuario/dio-desafio-twitter.git
cd dio-desafio-twitter

Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

Instale as dependências:
pip install -r requirements.txt


Configure as chaves de acesso do Twitter em src/secrets.py:
CONSUMER_KEY = "sua_consumer_key"
CONSUMER_SECRET = "sua_consumer_secret"
ACCESS_TOKEN = "seu_access_token"
ACCESS_TOKEN_SECRET = "seu_access_token_secret"


Inicie os serviços do Docker:
docker-compose up -d

Executando a Aplicação
Inicie a aplicação FastAPI:

python main.py


Acesse a API em http://127.0.0.1:8000/trends. Você precisará fornecer as credenciais de autenticação (username: admin, password: password).

Acesse o Mongo Express em http://127.0.0.1:8081 para visualizar os dados armazenados no MongoDB.

Acesse o dashboard Streamlit em http://127.0.0.1:8501 para visualizar as tendências do Twitter de forma interativa.

Geração de Relatórios
Para gerar um relatório em PDF das tendências, acesse a rota /generate_report:

curl -u admin:password http://127.0.0.1:8000/generate_report


O relatório será gerado como trends_report.pdf no diretório raiz do projeto.

Testes
Para rodar os testes unitários:
pytest teste/test_service.py


Contribuição
Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request.


### Observações

1. **Certifique-se de substituir o placeholder `https://github.com/seu-usuario/dio-desafio-twitter.git` pela URL real do seu repositório GitHub.**
2. **Verifique se todos os caminhos e instruções estão corretos e funcionam conforme esperado no seu ambiente de desenvolvimento.**
3. **Considere adicionar informações sobre como configurar as chaves de acesso do Twitter e outros detalhes específicos do projeto, se necessário.**

Este README deve fornecer uma visão abrangente do seu projeto, tornando mais fácil para outros desenvolvedores entenderem e utilizarem sua aplicação.
