import customtkinter as ctk
from banco import *
import pandas as pd

criar_tabela()


def atualizar_lista():

    lista.delete("1.0", "end")

    produtos = listar()

    for produto in produtos:
        lista.insert(
            "end",
            f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2]:.2f} | Qtde: {produto[3]}\n"
        )


def limpar_campos():
    entrada_nome.delete(0, "end")
    entrada_preco.delete(0, "end")
    entrada_quantidade.delete(0, "end")


def salvar_produto():

    try:

        nome = entrada_nome.get()
        preco = float(entrada_preco.get())
        quantidade = int(entrada_quantidade.get())

        cadastrar(nome, preco, quantidade)

        limpar_campos()

        atualizar_lista()

    except ValueError:
        print("Preencha os campos corretamente")


def excluir_produto():

    try:

        id_produto = int(entrada_id.get())

        excluir(id_produto)

        atualizar_lista()

        entrada_id.delete(0, "end")

    except ValueError:
        print("Digite um ID válido")


def editar_produto():

    try:

        id_produto = int(entrada_id.get())

        nome = entrada_nome.get()
        preco = float(entrada_preco.get())
        quantidade = int(entrada_quantidade.get())

        atualizar(
            id_produto,
            nome,
            preco,
            quantidade
        )

        atualizar_lista()

        limpar_campos()

        entrada_id.delete(0, "end")

    except ValueError:
        print("Preencha os campos corretamente")
        

def mostrar_estatisticas():

    produtos = listar()

    if not produtos:
        label_estatisticas.configure(
            text="Nenhum produto cadastrado."
        )
        return

    df = pd.DataFrame(
        produtos,
        columns=["ID", "Nome", "Preço", "Quantidade"]
    )

    texto = (
        f"Produtos: {len(df)} | "
        f"Preço Médio: R$ {df['Preço'].mean():.2f} | "
        f"Maior Preço: R$ {df['Preço'].max():.2f}"
    )

    label_estatisticas.configure(text=texto)
    
    
def exportar_excel():

    produtos = listar()

    if not produtos:
        label_estatisticas.configure(
            text="Não há produtos para exportar."
        )
        return

    df = pd.DataFrame(
        produtos,
        columns=["ID", "Nome", "Preço", "Quantidade"]
    )

    df.to_excel(
        "estoque.xlsx",
        index=False
    )

    label_estatisticas.configure(
        text="Arquivo estoque.xlsx criado com sucesso!"
    )


janela = ctk.CTk()

janela.title("Cadastro de Produtos")
janela.geometry("700x600")


titulo = ctk.CTkLabel(
    janela,
    text="Cadastro de Produtos",
    font=("Arial", 24)
)

titulo.pack(pady=10)


entrada_nome = ctk.CTkEntry(
    janela,
    placeholder_text="Nome do Produto",
    width=300
)

entrada_nome.pack(pady=5)

entrada_preco = ctk.CTkEntry(
    janela,
    placeholder_text="Preço",
    width=300
)

entrada_preco.pack(pady=5)

entrada_quantidade = ctk.CTkEntry(
    janela,
    placeholder_text="Quantidade",
    width=300
)

entrada_quantidade.pack(pady=5)

entrada_id = ctk.CTkEntry(
    janela,
    placeholder_text="ID do Produto",
    width=300
)

entrada_id.pack(pady=5)


frame_botoes = ctk.CTkFrame(janela)

frame_botoes.pack(pady=10)

botao_cadastrar = ctk.CTkButton(
    frame_botoes,
    text="Cadastrar",
    command=salvar_produto
)

botao_cadastrar.pack(side="left", padx=5)

botao_editar = ctk.CTkButton(
    frame_botoes,
    text="Editar",
    command=editar_produto
)

botao_editar.pack(side="left", padx=5)

botao_excluir = ctk.CTkButton(
    frame_botoes,
    text="Excluir",
    command=excluir_produto
)

botao_excluir.pack(side="left", padx=5)


botao_estatisticas = ctk.CTkButton(
    frame_botoes,
    text="Estatísticas",
    command=mostrar_estatisticas
)

botao_estatisticas.pack(side="left", padx=5)


botao_exportar = ctk.CTkButton(
    frame_botoes,
    text="Exportar Excel",
    command=exportar_excel
)

botao_exportar.pack(side="left", padx=5)


lista = ctk.CTkTextbox(
    janela,
    width=650,
    height=300
)

lista.pack(pady=15)

label_estatisticas = ctk.CTkLabel(
    janela,
    text=""
)

label_estatisticas.pack(pady=10)


atualizar_lista()


janela.mainloop()