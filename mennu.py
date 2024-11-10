
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

    print("seus produtos cadastrados", produtos)
    return produtos

       
cadastrar_produto()

        




        




    
                






