# Classe Contato
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

# Lista de contatos
contatos = []

# Função para adicionar um contato
def adicionar_contato(nome, telefone, email):
    novo_contato = Contato(nome, telefone, email)
    contatos.append(novo_contato)
    print(f"Contato {nome} adicionado com sucesso.")

# Função para buscar um contato
def buscar_contato(criterio):
    for contato in contatos:
        if contato.nome == criterio or contato.telefone == criterio or contato.email == criterio:
            return contato
    return None


def gerenciar_agenda():
    while True:
        acao = input(
            "Digite 'adicionar' para adicionar um contato, 'buscar' para buscar um contato ou 'sair' para sair: ").strip().lower()

        if acao == 'sair':
            print("Agenda finalizada.")
            break
        elif acao == 'adicionar':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            adicionar_contato(nome, telefone, email)
        elif acao == 'buscar':
            criterio = input("Digite o nome, telefone ou email para buscar: ").strip()
            contato = buscar_contato(criterio)
            if contato:
                print(f"{criterio} já está cadastrado.")
                print(contato)
            else:
                print("Contato não cadastrado.")
                adicionar_novo = input("Adicione contato: (sim/não): ").strip().lower()
                if adicionar_novo == 'sim':
                    nome = input("Digite o nome: ")
                    telefone = input("Digite o telefone: ")
                    email = input("Digite o email: ")
                    adicionar_contato(nome, telefone, email)
        else:
            print("Opção inválida.")


# Executar a função principal
gerenciar_agenda()

