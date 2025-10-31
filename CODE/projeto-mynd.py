import webbrowser
import os

def abrir_pagina(pagina):
    caminho = os.path.abspath(pagina)
    webbrowser.open_new_tab(f"file://{caminho}")
    print(f"✅ Página '{pagina}' aberta no navegador!")

def menu():
    print("\n🌐 MYND APP - Interface Local")
    print("1 - Tela de Boas-vindas")
    print("2 - Cadastro de Paciente")
    print("3 - Cadastro de Profissional")
    print("0 - Sair")

    while True:
        opcao = input("\nDigite o número da opção: ")

        if opcao == "1":
            abrir_pagina("welcome.html")
        elif opcao == "2":
            abrir_pagina("cadastro_paciente.html")
        elif opcao == "3":
            abrir_pagina("cadastro_profissional.html")
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
