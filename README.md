# Projeto de Dicionário de termos de informática.

Esse é projeto final da disciplina Projeto Integrador em computação III da Univesp.
- Contempla um processo de extração de dados de um dicionário de termos de informática em pdf;
- A criação e conexão com um banco de dados na cloud mongodb;
- Disponibilização de imagem da estrutura do projeto na cloud do dockerhub;
- Integração Contínua e Deploy Contínuo com o Github utilizando Github workflows;
- Uma página WEB para consulta dos termo que utiliza Javascript conectado através do Framework Django.


## Como Executar o Projeto

- É necessário baixar a imagem do dockerhub:

```bash
docker pull franscopel/django:v5
```

- É necessário baixar a versão do projeto do github

```bash
git pull git@github.com:Franscopel/integrador_3.git
```

- É necessário criar na raíz do projeto os seguintes variáveis de ambiente.
MONGO_URI
MONGO_DB_NAME
MONGO_COLLECTION


- É necessário executar via terminal na raíz do projeto, o comando:
```bash
python manage.py runserver
```
