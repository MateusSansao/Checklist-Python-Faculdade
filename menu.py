lista_de_tarefas = []

def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    data_de_criacao = input("Digite a data de criação (dd/mm/aaaa): ")
    status = input("Digite o status da tarefa (pendente/concluída): ")
    prazo_final = input("Digite o prazo final (dd/mm/aaaa): ")
    urgencia = input("Digite a urgência da tarefa (baixa/média/alta): ")

    lista_de_tarefas.append({
        "descricao": descricao,
        "data_de_criacao": data_de_criacao,
        "status": status,
        "prazo_final": prazo_final,
        "urgencia": urgencia
    })

    print(f"Tarefa '{descricao}' adicionada com sucesso!")


def listar_tarefas():
    if not lista_de_tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for index, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f"{index}. {tarefa['descricao']} - Status: {tarefa['status']} - Prazo: {tarefa['prazo_final']} - Urgência: {tarefa['urgencia']}")

def marcar_concluida():
    listar_tarefas()
    numero_tarefa = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
    
    if 1 <= numero_tarefa <= len(lista_de_tarefas):
        lista_de_tarefas[numero_tarefa - 1]['status'] = 'concluída'
        print(f"Tarefa '{lista_de_tarefas[numero_tarefa - 1]['descricao']}' marcada como concluída.")
    else:
        print("Número de tarefa inválido.")

def remover_tarefa():
    listar_tarefas()
    numero_tarefa = int(input("Digite o número da tarefa que deseja remover: "))
    
    if 1 <= numero_tarefa <= len(lista_de_tarefas):
        tarefa_removida = lista_de_tarefas.pop(numero_tarefa - 1)
        print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso.")
    else:
        print("Número de tarefa inválido.")


while True:
    opcao = input(
        "\nDigite a opção desejada:\n"
        "1 - Adicionar Tarefa\n"
        "2 - Listar Tarefas\n"
        "3 - Marcar Tarefa como concluída\n"
        "4 - Remover Tarefa\n"
    )

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "4":
        remover_tarefa()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")












    