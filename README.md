# Sistema de Gestão de Estoque (SGE)

Este projeto é um **Sistema de Gestão de Estoque** desenvolvido em Python, utilizando o framework Django. O objetivo é permitir o gerenciamento eficiente de produtos, entradas e saídas de mercadorias, além de categorias, fornecedores, marcas, entre outros aspectos relacionados ao controle de estoque.

## Funcionalidades
- Gerenciamento de produtos e categorias
- Controle de entradas e saídas de mercadorias
- Registro e consulta de fornecedores
- Administração de marcas e categorias

## Requisitos
- Python 3.x
- Django 3.x
- Banco de dados relacional (MySQL, PostgreSQL, etc.)

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/pasklan/sge.git
   ```
   
2. Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```

3. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## Estrutura do Projeto
- `app/` - Contém o código principal da aplicação.
- `inflows/` - Módulo responsável pelas entradas do estoque.
- `outflows/` - Módulo responsável pelas saídas do estoque.
- `products/` - Gerenciamento de produtos e categorias.
- `suppliers/` - Controle de fornecedores.

## Contribuições
Contribuições são bem-vindas! Para colaborar:
1. Faça um fork do projeto.
2. Crie um branch para sua funcionalidade ou correção
3. Envie um Pull Request com suas alterações.
