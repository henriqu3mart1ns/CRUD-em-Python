# 🛒 Sistema de Cadastro de Produtos

Projeto desenvolvido em Python utilizando **CustomTkinter**, **SQLite** e **Pandas** para realizar o gerenciamento de produtos de supermercado através de uma interface gráfica.

## 📋 Funcionalidades

* Cadastrar produtos
* Listar produtos cadastrados
* Editar produtos existentes
* Excluir produtos
* Exibir estatísticas dos produtos cadastrados
* Exportar os dados para uma planilha Excel
* Armazenamento local utilizando SQLite

## 🛠 Tecnologias Utilizadas

* Python
* CustomTkinter
* SQLite
* Pandas
* OpenPyXL

## 📁 Estrutura do Projeto

```text
projeto/
│
├── main.py
├── banco.py
├── produtos.db
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Acessar a pasta do projeto

```bash
cd nome-do-projeto
```

### 3. Instalar as dependências

Caso ainda não possua as bibliotecas instaladas, execute:

```bash
py -m pip install -r requirements.txt
```

ou

```bash
python -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém todas as bibliotecas necessárias para executar o projeto em outro computador.

### 4. Executar a aplicação

```bash
py main.py
```

ou

```bash
python main.py
```

## 📊 Estatísticas

O sistema utiliza a biblioteca Pandas para gerar informações como:

* Quantidade total de produtos
* Preço médio dos produtos
* Maior preço cadastrado

## 📈 Exportação para Excel

Ao clicar no botão **Exportar Excel**, será criado automaticamente um arquivo:

```text
estoque.xlsx
```

contendo todos os produtos cadastrados no sistema.

## 💾 Banco de Dados

O projeto utiliza SQLite para armazenamento local dos dados.

O banco é criado automaticamente na primeira execução do sistema.

## 👨‍💻 Autor

Projeto desenvolvido para fins de estudo e prática de:

* CRUD
* Python
* Banco de Dados SQLite
* Interface Gráfica com CustomTkinter
* Manipulação de Dados com Pandas
* Versionamento com Git e GitHub
