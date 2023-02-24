import textwrap

def menu():
menu = """\n
======= MENU ==========
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nc]\tNova conta
[lc]\tListar contas
[nu]\tNovo usuário
[q]\tSair
=> """

return input(textwrapp.dedent(menu))

def depositar(saldo, valor, extrato, /):
      if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")

      else:
            print("Operação Falhou! O valor informado é inválido.")

      return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
     
     excedeu_saldo = valor > saldo
     excedeu_limite = valor > limite
     excedeu_saques = numero_saques>= limite_saques

     if excedeu_saldo:
          print("\n Operação Falhou! Você não tem saldo o sulficiente.")

     elif excedeu_limite:
          print("\n Operação Falhou! O valor do saque excedeu o limite.")

    elif excedeu_saques:
          print("\n Operação Falhou! Número de saques excedido.")

    elif valor >0:
        saldo -= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        numero_Saques+= 1
        print("\n Saque realizado com sucesso!")

    else:
          print("\n Operação Falhou! Valor inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
     print(" ======== Extrato =========")
     print("Não foram realizadas movimentaçõe"if not extrayo else extrato)
     print(f"\nSaldo:\t\tR$ {saldo:.2f}")

def criar_usuario(usuarios)
     cpf = input("Informe o CPF (Somente números): ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("\n Já existe usuário com este CPF")
          return 

     nome = input("Informe o nome completo:")
     data_nascimento = inpit("Informe a data de mascimento (dd-mm-aaaa): ")     
     endereco = input("Informe o endereço (Rua, nro - bairro - cidade/estado sigla:")

     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

     print(" Usuario criado com sucesso")

def filtrar_usuarios(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuario if usuario["cpf"] = cpf]
    return usuarios_filtrados [0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF do usuario: ")
     usuario = filtrar+usuario(cpf, usuarios)

     if usuario:
          print("\n Conta criada com sucesso")
          return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     
     print("Usuário não encontrado, fluxo de criação de conta encerrado.")

def listar_contas(contas):
     for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['none']}
        """
    print("=" * 100)
    print(textwrap.dedent(linha))

def main():
      LIMITE_SAQUES = 3
      AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

while True:
    opcao = menu()
    
    if opcao == "d":
        valor = float(input("Informe o valor do Depósito:"))
        
        saldo, extrato = depositar(saldo=saldo, valor=valor, extrato=extrato)

    elif opcao == "s":
        
    valor = float(input("Informe o valor do saque:"))
    
        saldo, extrato = sacar(
         saldo=saldo,
         valor=valor,
         extrato=extrato,
         limite=limite,
         numero_saques=numero=saques,
         limite_saques=LIMITE_SAQUES,
        )
        
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        numer_conta = len(contas) = 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
         contas.append(Conta)

    elif opcao == "lc":
        listar_contas(contas)


    elif opcao == "q":
        break
    
    else:        
        print("Operação inválida, por favor selecione novamente a operação desejada")
    
main()        
    
        