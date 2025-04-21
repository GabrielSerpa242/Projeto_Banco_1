menu = '''
======= MENU =======
       
       [d] Depositar
       [s] Saldo
       [e] Extrato
       [q] Sair

=====================

==> ''' 
saldo = 0
limite = 500 
extrato = '' '' 
numero_saques = 0
LIMITES__SAQUES = 3 
while True:
    
    opcao = input(menu)
    
    if open == 'd':
            
        valor = float(input('Informe o valor: ')) 
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n' 
        else: 
            print('Opção inválida digite novamente')
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: ')) 
        excedeu_saldo = valor>saldo 
        excedeu_limite = valor>saldo 
        excedeu_saques = numero_saques >= LIMITES__SAQUES 
        if excedeu_saldo:
            print('Operação falhou não tem tem saldo suficiente') 
        
        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')
        elif excedeu_saques:
            print('Operação falhou! O número máximo de tentativas.')
        elif valor > 0:
            saldo += valor
            extrato == f'Saque: R$ {valor:.2f}\n'
        
        else:
            print('Operação falhou! O valor informado é inválido.')
    elif opcao == 'e':
        print('\n ===== EXTRATO =====')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('===================') 
    elif opcao == 'q':
        break 
    else:
        print('Operação inválida, por favor selecione novamente a operação.')