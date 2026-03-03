class Banco:
    def __init__(self, cpf, nome, saldo_inicial):
        self.cpf = cpf
        self.nome = nome
        self.saldo = saldo_inicial

    # 1️⃣ Saque
    def saque(self):
        valor = float(input("Digite o valor para saque: R$ "))
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")
        print(f"Saldo atual: R${self.saldo:.2f}\n")

    # 2️⃣ Depósito
    def deposito(self):
        valor = float(input("Digite o valor para depósito: R$ "))
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
        print(f"Saldo atual: R${self.saldo:.2f}\n")

    # 3️⃣ Poupança
    def poupanca(self):
        valor = float(input("Digite o valor para aplicar na poupança: R$ "))
        if valor > 0:
            self.saldo += valor
            print(f"Poupança de R${valor:.2f} adicionada.")
        else:
            print("Valor inválido.")
        print(f"Saldo atual: R${self.saldo:.2f}\n")

    # 4️⃣ Empréstimo
    def emprestimo(self):
        valor = float(input("Digite o valor da parcela do empréstimo: R$ "))
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Parcela de empréstimo de R${valor:.2f} paga.")
        else:
            print("Saldo insuficiente ou valor inválido.")
        print(f"Saldo atual: R${self.saldo:.2f}\n")

    # 5️⃣ PIX Depósito
    def pixdeposito(self):
        valor = float(input("Digite o valor do PIX recebido: R$ "))
        if valor > 0:
            self.saldo += valor
            print(f"PIX recebido no valor de R${valor:.2f}.")
        else:
            print("Valor inválido.")
        print(f"Saldo atual: R${self.saldo:.2f}\n")

    # 6️⃣ PIX Transferência
    def pixtransferencia(self):
        valor = float(input("Digite o valor do PIX a enviar: R$ "))
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"PIX enviado no valor de R${valor:.2f}.")
        else:
            print("Saldo insuficiente ou valor inválido.")
        print(f"Saldo atual: R${self.saldo:.2f}\n")


# 🔎 Cadastro do cliente
cpf = input("Digite o CPF: ")
nome = input("Digite o nome do cliente: ")
saldo_inicial = float(input("Digite o saldo inicial: R$ "))

cliente = Banco(cpf, nome, saldo_inicial)

# 🔹 Menu simples
while True:
    print("===== MENU =====")
    print("1 - Saque")
    print("2 - Depósito")
    print("3 - Poupança")
    print("4 - Empréstimo")
    print("5 - PIX Depósito")
    print("6 - PIX Transferência")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cliente.saque()
    elif opcao == "2":
        cliente.deposito()
    elif opcao == "3":
        cliente.poupanca()
    elif opcao == "4":
        cliente.emprestimo()
    elif opcao == "5":
        cliente.pixdeposito()
    elif opcao == "6":
        cliente.pixtransferencia()
    elif opcao == "0":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida!\n")