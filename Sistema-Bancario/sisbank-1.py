menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

***LEMBRETE => USE PONTO PARA CASA DECIMAIS! ***

=>"""

saldo = 0
limite = 500
extrato = "SALDO INICIAL R$"+str(float(saldo))
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    opcao = int(opcao)

    if opcao == 1:
        condicao = True
        while condicao == True:
            deposito = input("Informe o valor a ser depositado na conta: ")
        
            if deposito == "":
                print("Deposito não pode ser vazio, informe o valor do deposito: ")
                print(deposito)

            elif float(deposito) > 0:
                saldo = saldo + float(deposito)
                extrato = extrato + "\nDeposito R$" + str(float(deposito))
                print("Deposito realizado!") 
                condicao = False

            else:
                print("Valor do deposito inválido, informe um valor válido:")
    
    elif opcao == 2:
        condicao = True
        while condicao == True:
            saque = input("Informe o valor que deseja sacar: ")
            
            if saque == "":
                print("Nenhuma valor digitado.\n")
                
            elif float(saque) <= 0:
                saque = float(saque)
                print("Saque não pode ser negativo ou igual a Zero.")
            
            elif float(saque) <= limite:
                saque = float(saque)
                if saque <= saldo:
                    if numero_saques < LIMITE_SAQUES:
                        saldo = saldo - saque
                        numero_saques += 1
                        extrato = extrato + "\nSaque -R$" + str(float(saque))
                        print("Saque Realizado!")
                        condicao = False
                        
                    else:
                        print("Quantidade de saque diario excedida, realize o saque no proximo dia util!")
                        condicao = False         
                    
                else:
                    print("Saque não pode ser realizado, pois o valor de saque é maior que o saldo disponível em conta!")                
                
            else:
                print(f"Saque não pode exceder o limite por operação, que é R$ {float(limite)}")

            
    
    elif opcao == 3:
        if extrato == "SALDO INICIAL R$0.0":
            print("Ainda não foram realizadas movimentação na conta!")
        else:
            extrato = extrato + "\nSALDO ATUAL R$" + str(float(saldo))
            print(extrato)
    
    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")