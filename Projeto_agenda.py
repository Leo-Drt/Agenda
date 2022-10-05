from distutils.log import debug
import email
import readline


AGENDA = {}


def mostrar_contatos():
    if AGENDA:
        for contatos in AGENDA:
            buscar_contato(contatos)
            print("------- / -------- / ------")
    else:
        print("Agenda Vazia!")

def buscar_contato(contatos):
    try:
        print("Nome:", contatos)
        print("Telefone", AGENDA[contatos]['telefone'])
        print("Email", AGENDA[contatos]['email'])
        print("Endereço", AGENDA[contatos]['endereco'])

    except KeyError:
        print("Contato inexistente")
    
    except Exception as error:
        print("Ocorreu um erro inexperado!")
        print(error)

def ler_detalhes_contatos():
    telefone= input("Digite o telefone do contato: ")
    email= input("Digite o email do contato: ")
    endereco= input("Digite o endereço do contato: ")
    return telefone, email, endereco 

def incluir_editar_contato(contatos, telefone, email, endereco):
    AGENDA[contatos]= {
        "telefone" : telefone,
        "email": email,
        "endereco": endereco
        }
    salvar()
    print(">>> Contato {} foi adicionado/editado a sua agenda".format(contatos))

def excluir_contato(contatos):
    try:
        AGENDA.pop(contatos)
        salvar()
        print(">>> Contato {} foi excluído da sua agenda".format(contatos))
        print()
    
    except KeyError:
        print("Contato inexistente")
    
    except Exception as error:
        print("Ocorreu um erro inexperado!")
        print(error)

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo,"w") as arquivo:
            for contatos in AGENDA:
                telefone = AGENDA[contatos]['telefone']
                email = AGENDA[contatos]['email']
                endereco = AGENDA[contatos]['endereco']
                arquivo.write("{}; {}; {}; {}\n".format(contatos, telefone, email, endereco))

        print("Agenda exportada com sucesso!")

    except Exception as error:
        print("Ocorreu algum erro ao exportar os contatos!")
        print(error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas= arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';')
            
                nome= detalhes[0]
                telefone= detalhes[1]
                email= detalhes[2]
                endereco= detalhes[3]
                incluir_editar_contato(nome, telefone, email, endereco)

    except FileNotFoundError:
        print("Arquivo não encontrado!")

    except Exception as error:
        print("Algo inesperado aconteceu!")
        print(error)

def salvar():
    exportar_contatos("database.txt")

def carregar():
    try:
        with open("database.txt", 'r') as arquivo:
            linhas= arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';')
            
                nome= detalhes[0]
                telefone= detalhes[1]
                email= detalhes[2]
                endereco= detalhes[3]
                AGENDA[nome]={
                    "telefone": telefone,
                    "email": email,
                    "endereco": endereco
                }

            print("Database carregado com sucesso !")
            print("{} contatos carregados".format(len(AGENDA)))

    except FileNotFoundError:
        print("Arquivo não encontrado!")

    except Exception as error:
        print("Algo inesperado aconteceu!")
        print(error)
    

def menu():
        print("------------------------------------")
        print("Menu de contato agenda")
        print("1 - Mostrar todos os contatos")
        print("2 - Buscar contato")
        print("3 - Adicionar contato")
        print("4 - Editar contato")
        print("5 - Excluir contato")
        print("6 - Exportar contato para CSV")
        print("7 - Importar contatos para CSV")
        print("0 - Fechar agenda de contatos")
        print("------------------------------------")


## Início do Programa.
carregar()
while True:
    
    menu()

    opcao= input("Escolha uma opção: ")
    if opcao == "1":
        mostrar_contatos()
        print()

    elif opcao == "2":
        contatos= input("Digite o nome do contato: ")
        buscar_contato(contatos)
        print()

    elif opcao == "3":
        contatos= input("Digite o nome do contato:")
        try:
            AGENDA[contatos]
            print("Contato existente!")
        except KeyError:
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(contatos, telefone, email, endereco)

    elif opcao == "4":       
        contatos= input("Digite o nome do contato:")
        try:
            AGENDA[contatos]
            print("Editando contato", contatos)
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(contatos, telefone, email, endereco)
        except KeyError:
            print("Contato inexistente!")

    elif opcao == "5":
        contatos= input("Digite o nome do contato que quer excluir: ")
        excluir_contato(contatos)

    elif opcao == "6":
        nome_do_arquivo = input("Digite o nome do arquivo a ser exportado: ")
        exportar_contatos(nome_do_arquivo)

    elif opcao == "7":
        nome_do_arquivo = input("Digite o nome do arquivo a ser importado: ")
        importar_contatos(nome_do_arquivo)

    elif opcao == "0":
        print("Fechando a agenda !")
        break

    else:
        print("comando inválido !!")