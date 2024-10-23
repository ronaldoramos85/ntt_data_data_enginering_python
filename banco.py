from datetime import datetime
# Menu informativo sobre as opcoes validas
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Inicializacao de variaveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10
mascara_ptbr = "%d/%m/%Y %H:%M"
# Finalizacao de variaveis

# Inicio do laco principal de execucao do programa
while True:
    
    data_hora_operacao = datetime.now().strftime(mascara_ptbr)

    # Le a opcao
    opcao = input(menu)
    
    # Verifica se a opcao eh string e de um unico caracter
    if isinstance(opcao, str) and len(opcao) == 1:

        # Inicio do deposito
        if opcao == "d":
            
            # Le o valor de deposito
            valor = float(input("Informe o valor do depósito: "))

            # Testa se o valor eh positivo
            if valor > 0:
                
                # Adiciona o valor ao saldo
                saldo += valor
                
                # Concatena a operacao de deposito efetuada ao extrato
                extrato += f"(+) Depósito: R$ {valor:.2f} às {data_hora_operacao}\n"

            # Se o valor de opcao digitado eh invalido retorna uma mensagem de erro
            else:
                print("Operação falhou! O valor informado para depósito é zero ou negativo.")
        # Fim do deposito
        
        # Inicio do saque
        elif opcao == "s":
            
            # Le o valor do saque
            valor = float(input("Informe o valor do saque: "))

            # Verificacao se valor do saque eh maior que o saldo
            excedeu_saldo = valor > saldo

            # Verificacao se o valor do saque eh maior que o limite por operacao
            excedeu_limite = valor > limite

            # Verificacao se o numero de saques excede o limite para essa operacao
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            # Verifica se o valor do saque excede o saldo e mostra uma mensagem de erro se esse for o caso
            if excedeu_saldo:
                print("Operação falhou! O valor do saque excede o valor do saldo em conta.")

            # Verifica se o valor do saque excede o limite por operacao e mostra uma mensagem de erro se esse for o caso
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite por operação.")

            # Verifica se o numero de saques excede o limite para essa operacao e mostra uma mensagem de erro se esse for o caso
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            # Se o valor do saque for positivo o valor eh debitado do saldo e uma linha relativa ah operacao eh adicionada ao extrato
            elif valor > 0:
                saldo -= valor
                extrato += f"(-) Saque: R$ {valor:.2f} às {data_hora_operacao}\n"
                # Eh adicionado um saque ao numero de saques para controle do limite de vezes desta operacao
                numero_saques += 1

            # Exibe mensagem de erro se o valor do saque informado nao eh positivo
            else:
                print("Operação falhou! O valor informado para depósito é zero ou negativo.")
        # Fim do saque
        
        # Inicio do extrato
        elif opcao == "e":
            # Exibe as operacoes acumuladas ate o momento no extrato caso exista alguma. Caso nao exista qualquer operacao, eh exibida uma mensagem informando que nenhuma movimentacao foi realizada
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}  às {data_hora_operacao}")
            print("==========================================")
        # Fim do extrato
        
        # Se pressionar 'q' como opcao o programa finaliza sua execucao
        elif opcao == "q":
            break

        # Se a letra digitada nao corresponde a nenhuma das operacoes validas eh exibida uma mensagem que informa isso 
        else:
            print("Operação inválida. Por favor, selecione uma das opções válidas de operações.")
    
    # Exibe uma mensagem de erro caso nao seja digitada um caracter valido
    else:
        print("Operação inválida! Você não digitou uma das letras válidas de operação.")

# Fim do laco de execucao do programa