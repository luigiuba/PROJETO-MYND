import json
import os
import webbrowser

# Caminho do banco local
ARQUIVO_CADASTRO = "cadastros.json"

# === Função para salvar dados ===
def salvar_cadastro(tipo, dados):
    """Salva dados de paciente ou profissional em um arquivo JSON local."""
    if os.path.exists(ARQUIVO_CADASTRO):
        with open(ARQUIVO_CADASTRO, "r", encoding="utf-8") as f:
            cadastros = json.load(f)
    else:
        cadastros = {"pacientes": [], "profissionais": []}

    cadastros[tipo].append(dados)

    with open(ARQUIVO_CADASTRO, "w", encoding="utf-8") as f:
        json.dump(cadastros, f, ensure_ascii=False, indent=4)
    
    print(f"✅ Novo {tipo[:-1]} salvo com sucesso!")

# === Menu principal ===
def menu():
    print("\n🌐 MYND APP - Interface Local")
    print("1 - Tela de Boas-vindas")
    print("2 - Cadastrar Paciente")
    print("3 - Cadastrar Profissional")
    print("4 - Ver Cadastros Salvos")
    print("0 - Sair")

    while True:
        opcao = input("\nDigite o número da opção: ")

        if opcao == "1":
            abrir_pagina("welcome.html")

        elif opcao == "2":
            dados = coletar_dados("paciente")
            salvar_cadastro("pacientes", dados)

        elif opcao == "3":
            dados = coletar_dados("profissional")
            salvar_cadastro("profissionais", dados)

        elif opcao == "4":
            mostrar_cadastros()

        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida, tente novamente.")
            elif opcao == "5":
    abrir_pagina("login.html")


# === Coleta de dados no terminal ===
def coletar_dados(tipo):
    print(f"\n📝 Cadastro de {tipo.capitalize()}")

    nome = input("Nome completo: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    senha = input("Senha: ")

    if tipo == "profissional":
        area = input("Área de atuação: ")
        return {"nome": nome, "email": email, "telefone": telefone, "senha": senha, "area": area}
    else:
        return {"nome": nome, "email": email, "telefone": telefone, "senha": senha}

# === Exibir cadastros existentes ===
def mostrar_cadastros():
    if not os.path.exists(ARQUIVO_CADASTRO):
        print("\n⚠️ Nenhum cadastro encontrado.")
        return

    with open(ARQUIVO_CADASTRO, "r", encoding="utf-8") as f:
        cadastros = json.load(f)

    print("\n📋 PACIENTES CADASTRADOS:")
    for p in cadastros["pacientes"]:
        print(f" - {p['nome']}
