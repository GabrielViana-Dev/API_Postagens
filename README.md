# Flask API de Gerenciamento de Postagens e Autores

Este é um exemplo de uma API construída com Flask para gerenciar postagens e autores. A API possui endpoints para criar, listar, atualizar e excluir postagens e autores, além de fornecer autenticação por token.

## Como Executar

1. Certifique-se de ter Python instalado em seu sistema.
2. Instale as dependências necessárias executando o comando:
3. Certifique-se de ter um banco de dados SQLite configurado. O arquivo `structureDatabase.py` contém as definições dos modelos do banco de dados.
4. Execute o arquivo `app.py`.
5. A API estará acessível em `http://localhost:5000`.

## Endpoints Disponíveis

### Autenticação

- `POST /login/`: Realiza o login do usuário e fornece um token de acesso.

### Postagens

- `GET /`: Lista todas as postagens.
- `GET /postagem/<id_postagem>/`: Obtém uma postagem específica pelo seu ID.
- `POST /postagem/`: Cria uma nova postagem.
- `PUT /postagem/<id_postagem>/`: Altera uma postagem existente.
- `DELETE /postagem/<id_postagem>/`: Exclui uma postagem existente.

### Autores

- `GET /autores/`: Lista todos os autores.
- `GET /autores/<id_autor>/`: Obtém informações de um autor específico pelo seu ID.
- `POST /autores/`: Cria um novo autor.
- `PUT /autores/<id_autor>/`: Altera informações de um autor existente.
- `DELETE /autores/<id_autor>/`: Exclui um autor existente.

## Autenticação por Token

A autenticação por token é necessária para acessar todos os endpoints relacionados a postagens e autores. O token deve ser enviado no cabeçalho da requisição como `x-access-token`.

