saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE = 3

while True:

    menu = input("""
######## MENU ########
            
[A] DEPOSITO
[B] SAQUE
[C] EXTRATO
[D] SAIR
        
""")
    
    if menu == "a" or menu == "A":
        x = float(input("Digite um valor para deposito: R$ "))
        saldo += x
        extrato += str(f'\n+ R$ {x}')
    elif menu == "b" or menu == "B":
        x = float(input("Digite um valor para saque: R$ "))

        if x > limite or num_saques > LIMITE:
            print("[ERRO] VALOR INVALIDO OU MAIOR QUE O ESPERADO.")
        else:
            saldo = saldo - x
            num_saques += 1
            extrato += str(f'\n- R$ {x}')
    elif menu == "c" or menu == "C":
        print(f"""######## SUA CONTA ########
SALDO: {saldo}
EXTRATO: {extrato}
SAQUES: {num_saques}
LIMITE DE SAQUES: {LIMITE}""")
    elif menu == "d" or menu == "D":
        print("######## FINALIZANDO O PROGRAMA ########")
        break
    else:
        print("##### [ERRO] OPERACAO INVALIDA #####")