import json
import time
from pathlib import Path
import os

compras = {}

def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade

def remover_item(compras, item):
    if item in compras:
        del compras[item]

def visualizar_compras(compras):
    for item, quantidade in compras.items():
        print(f'{item}: {quantidade}')
    print()
    print('Pressione qualquer tecla para continuar...')
    input()

def salvar_compras(compras, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(compras, arquivo)

def carregar_compras(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        return json.load(arquivo)

def gerenciar_compras(compras, nm_arquivo=None):
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print('1. Adicionar Item')
        print('2. Remover Item')
        print('3. Visualizar Lista')
        print('4. Salvar e sair')
        print('5. Sair sem salvar')

        selecao = input("Escolha uma opção: ")

        if selecao == '1':
            item = input('Digite o item:')
            qtde = float(input('Digite a quantidade:'))
            adicionar_item(compras, item, qtde)
        elif selecao == '2':
            item = input('Digite o item:')
            remover_item(compras, item)
        elif selecao == '3':
            visualizar_compras(compras)
        elif selecao == '4':
            if nm_arquivo is None:
                nm_arquivo = input ("Digite o nome do arquivo: ")
            if not nm_arquivo.endswith(".json"):
                nm_arquivo += ".json"
            salvar_compras(compras, nm_arquivo)
            break
        elif selecao == '5':
            break
        else:
            print ("Seleção inválida!")
            time.sleep(2)

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print('1. Criar uma nova lista de compras')
        print('2. Carregar uma lista existente')
        print('3. Sair')

        opcao_main = input('Escolha uma opção: ')

        if opcao_main not in ('1', '2', '3'):
            print('Opção inválida!')
            print()
            time.sleep(2)

        if opcao_main == '1':
            compras = {}
            gerenciar_compras(compras)

        if opcao_main == '2':
            print('Listas disponíveis:')
            #caminho = Path.cwd()
            #arquivos = caminho.iterdir()

            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith('.json')]
            # Tratamento de arquivos não encontrados
            if not arquivos:
                print ('Nenhuma lista encontrada!')
                time.sleep(3)
                continue

            for i, arquivo in enumerate(arquivos,1):
                print(f'{i} {arquivo}')

            escolha = int(input("Escolha a lista para carregar (0 se nenhuma)"))
            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print('Opção inválida!')
                time.sleep(3)
                continue

            compras = carregar_compras(arquivos[escolha - 1])
            gerenciar_compras(compras, arquivos[escolha -1])
        
        if opcao_main == '3':
            break

if __name__ == "__main__":
    main()

