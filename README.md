# To-Do Flask App

Um simples aplicativo de lista de tarefas (To-Do List) construído com Python, Flask e PostgreSQL. Este projeto foi criado como um exercício prático para aprender os fundamentos do desenvolvimento web com o framework Flask, incluindo rotas, templates com Jinja2, e interações com banco de dados usando SQLAlchemy.

## Funcionalidades

-   **Criar** novas tarefas.
-   **Ler** e exibir a lista de tarefas existentes.
-   **Atualizar** tarefas (implementação futura).
-   **Deletar** tarefas (implementação futura).

## Tecnologias Utilizadas

-   **Back-end:** Python 3
-   **Framework:** Flask
-   **ORM:** Flask-SQLAlchemy
-   **Banco de Dados:** PostgreSQL
-   **Front-end:** HTML5, CSS3

## Pré-requisitos

Antes de começar, você precisa ter instalado em sua máquina:
-   [Python 3](https://www.python.org/downloads/)
-   [PostgreSQL](https://www.postgresql.org/download/)
-   Git (para clonar o repositório)

## Como Configurar e Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/todo-flask.git](https://github.com/seu-usuario/todo-flask.git)
    cd todo-flask
    ```

2.  **Instale as dependências:**
    (Recomendado fazer dentro de um ambiente virtual)
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure o Banco de Dados PostgreSQL:**
    -   Certifique-se de que o serviço do PostgreSQL está rodando.
    -   Crie um novo banco de dados (ex: `todoflaskdb`).
    -   Verifique se o usuário e a senha correspondem aos que estão configurados no arquivo `app/__init__.py`.

4.  **Configure a Aplicação Flask:**
    -   No terminal, defina a variável de ambiente para o aplicativo Flask.
    ```bash
    # No Windows (PowerShell)
    set FLASK_APP=run.py
    
    # No Mac/Linux
    export FLASK_APP=run.py
    ```

5.  **Crie as Tabelas no Banco de Dados:**
    -   Execute o shell interativo do Flask:
    ```bash
    flask shell
    ```
    -   Dentro do shell, execute os seguintes comandos para criar as tabelas:
    ```python
    from app import db
    db.create_all()
    exit()
    ```

6.  **Execute a Aplicação:**
    ```bash
    python run.py
    ```
    -   A aplicação estará rodando em `http://127.0.0.1:5000/`.

## Estrutura do Projeto

```
/
├── app/                  # Pacote principal da aplicação
│   ├── static/           # Arquivos estáticos (CSS, JS, Imagens)
│   │   └── css/
│   │       └── style.css
│   ├── templates/        # Templates HTML (Jinja2)
│   │   └── home.html
│   ├── __init__.py       # Inicializador da aplicação (Application Factory)
│   ├── models.py         # Modelos de dados do SQLAlchemy
│   └── routes.py         # Rotas e lógica das views
├── run.py                # Ponto de entrada para executar a aplicação
├── requirements.txt      # Lista de dependências Python
└── README.md             # Documentação do projeto
