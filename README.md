# app-project-django

Um projeto Django básico.

## Funcionalidades

* Página inicial
* Página Sobre
* Página de Contato
* Uma página que cumprimenta o usuário pelo nome.
* Uma página para registrar mensagens.

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`:

* asgiref==3.9.2
* Django==5.2.7
* sqlparse==0.5.3
* tzdata==2025.2

## Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd app-project-django
   ```
3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows, use `.venv\Scripts\activate`
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

## Uso

Para iniciar o servidor de desenvolvimento, execute o seguinte comando:

```bash
python manage.py runserver
```

O aplicativo estará disponível em `http://127.0.0.1:8000/`.

## Licença

Este projeto está licenciado sob os termos do arquivo `LICENSE`.
