import textwrap

###Menu do sistema.
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuario
[5] Nova Conta
[6] Listar Contas
[0] Sair

***LEMBRETE => USE PONTO PARA CASA DECIMAIS! ***

=>"""


##Metodo de Saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, condicao): 
    if valor == "":
        print("Nenhuma valor digitado.\n")
               
    elif float(valor) <= 0:
        saque = float(valor)
        print("Saque não pode ser negativo ou igual a Zero.")
            
    elif float(valor) <= limite:
        valor = float(valor)
        if valor <= saldo:
            if numero_saques < LIMITE_SAQUES:
                saldo = saldo - valor
                numero_saques += 1
                extrato = extrato + "\nSaque -R$" + str(float(valor))
                print("Saque Realizado!")
                condicao = False
                        
            else:
                print("Quantidade de saque diario excedida, realize o saque no proximo dia util!")
                condicao = False         
                  
        else:
            print("Saque não pode ser realizado, pois o valor de saque é maior que o saldo disponível em conta!")                
                
    else:
        print(f"Saque não pode exceder o limite por operação, que é R$ {float(limite)}")

    return saldo, extrato, condicao

### Metodo Deposito
def depositar(saldo, valor, extrato, condicao):
    if valor == "":
        print("Deposito não pode ser vazio!")

    elif float(valor) > 0:
        saldo = saldo + float(valor)
        extrato = str(extrato) + "\nDeposito +R$" + str(float(valor))
        print("Deposito realizado!") 
        condicao = False

    else:
        print("Valor do deposito inválido, informe um valor válido:")


    return saldo, extrato, condicao

###Metodo de Extrato
def extrato(saldo, /, extrato):
    if str(extrato) == "":
        print("Ainda não foram realizadas movimentação na conta!")
    else:
        extrato = str(extrato) + "\nSALDO ATUAL R$" + str(float(saldo))
        print(extrato)

### Metodo de criar usuario.
def criar_usuario(usuarios):
    cpf = input("Informe o CPF a ser cadastrado(somente os números!):")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Usuario já cadastrado na plaforma!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario criado com sucesso!")

### Metodo Filtrar usuario
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

###Metodo Criar conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("CPF não encontrado na base de dados, acesse criar um usuario!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
#####Variaveis uteis gerais no sistema.
saldo = 0
limite = 500
extrato_conta = "SALDO INICIAL R$"+str(float(saldo))
numero_saques = 0
usuarios = []
contas = []
LIMITE_SAQUES = 3
AGENCIA = "0001"

###Aplicação
while True:

    opcao = int(input(menu))

    if opcao == 1:
        condicao = True
        while condicao == True:
            deposito = input("Informe o valor a ser depositado na conta: ")
        
            saldo, extrato_conta, condicao = depositar(saldo, deposito, extrato_conta, condicao)
    
    elif opcao == 2:
        condicao = True
        while condicao == True:
            saque = input("Informe o valor que deseja sacar: ")
            saldo, extrato_conta, condicao = sacar(saldo=saldo, valor=saque, extrato=extrato_conta, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES, condicao=condicao)

    elif opcao == 3:
        extrato_conta = str(extrato_conta)
        extrato(saldo, extrato=extrato_conta)

    elif opcao == 4:
        criar_usuario(usuarios)
    
    elif opcao == 5:
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
                contas.append(conta)
                
    elif opcao == 6:
        listar_contas(contas)

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")
    








