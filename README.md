## Projeto de Busca por Contabilidade

**Descrição**

Este projeto consiste em uma aplicação web simples desenvolvida com Flask para realizar buscas por informações contábeis em um banco de dados SQLite local. O banco de dados é atualizado periodicamente por meio de uma API externa.

**Funcionalidades**

* Busca por informações contábeis por nome
* Exibe os resultados em uma tabela
* Atualiza automaticamente o banco de dados com informações da API externa

**Requisitos**

* Python instalado globalmente
* Pacotes Python:
    * Flask
    * requests

**Instalação**

1. Clone o repositório do projeto (se aplicável).
2. Instale os pacotes necessários:

```bash
pip install Flask
pip install requests
```

**Configuração**

1. Abra o arquivo `app.py`.
2. Verifique e configure as seguintes informações:
    * URL da API externa (se necessário)
    * Configurações adicionais específicas do projeto

**Execução**

1. Inicie o servidor Flask no diretório raiz do projeto:

```bash
python app.py
```

2. Acesse a aplicação no seguinte endereço:

```
http://127.0.0.1:5000/
```

3. Na página inicial, digite o nome da contabilidade desejada na barra de busca e clique em "Buscar".
4. A tabela será atualizada com os resultados correspondentes às informações da contabilidade pesquisada.

**Estrutura do Projeto**

* `app.py`: Contém o código principal da aplicação Flask.
* `status.db`: Banco de dados SQLite que armazena as informações de status.
* `templates/`: Pasta que contém o arquivo HTML para a interface web.
* `static/` (opcional): Pasta para arquivos estáticos (CSS, JavaScript, imagens).

**Observações**

* O pacote `sqlite3` é parte da biblioteca padrão do Python e não requer instalação adicional.
* Este projeto é um exemplo básico e pode ser adaptado de acordo com suas necessidades específicas.
**Contribuições**

Sinta-se à vontade para contribuir com este projeto! Envie suas sugestões, pull requests ou issues no repositório do projeto.
