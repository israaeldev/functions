
# resultado = " "

# def menu():
#     while True:
#         opcao = input(
            
            
#             "1. Cadastrar produto\n"
#             "2. Listar produtos\n"
#             "3. atualizar produto\n"
#             "4. atualizar informações\n"
#             "5. Remover produto\n"
#             "6. sair do programa\n" 
#             "Escolha uma opção: "              
#         )
#         if opcao == 1:
            
def cadastrar_produto():
    produtos = []
    while True:    
        produto = input("digite o nome do produto que deseja cadastrar: ")
        produtos.append(produto)
    
        novo_cadastro = input("Deseja cadastrar novos produtos? (sim/nao)").lower()
        if novo_cadastro != "sim":
            break

    listar_produtos(produtos)


def listar_produtos(produtos):
    if not produtos:
        print("nenhum produto cadastrado")
    else:
        print("lista de produtos cadastrados")
        for produto in produtos:
            print(f"{produto}")
            
            

cadastrar_produto()

        




        




    
                






