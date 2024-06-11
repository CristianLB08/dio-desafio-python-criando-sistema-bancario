import re

# Banco de dados de clientes - matriz inicial com alguns dados fictícios
clientes = {
    12345678901: {"nome": "João Silva", "senha": "Senha123!", "saldo": 0, "extrato": "", "numero_saques": 0},
    10987654321: {"nome": "Maria Santos", "senha": "Senha456@", "saldo": 0, "extrato": "", "numero_saques": 0},
}

# Função para validar a senha
def validar_senha(senha):
    if len(senha) < 10 or len(senha) > 20:
        return False
    if not re.search(r'\d', senha):
        return False
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'[a-z]', senha):
        return False
    if not re.search(r'[!@#$%¨&*()_+\-=\[\]{};:"\\|,.<>\/?]', senha):
        return False
    return True

# Função para criar uma nova conta
def criar_conta():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = int(input("CPF (apenas números): "))

    while True:
        senha = input("Crie uma senha: ")
        if validar_senha(senha):
            break
        else:
            print("Senha inválida! A senha deve ter entre 10 e 20 caracteres, incluindo pelo menos um número, uma letra maiúscula, uma letra minúscula e um caractere especial.")

    clientes[cpf] = {"nome": f"{nome} {sobrenome}", "senha": senha, "saldo": 0, "extrato": "", "numero_saques": 0}
    print("Conta criada com sucesso!")
    return cpf

# Função para autenticar o cliente
def autenticar_cliente(cpf):
    for _ in range(3):
        senha = input("Digite sua senha: ")
        if senha == clientes[cpf]["senha"]:
            return True
        else:
            print("Senha incorreta. Tente novamente.")
    print("Número máximo de tentativas excedido. Saindo do sistema.")
    return False

# Função principal do sistema bancário
def sistema_bancario(cpf):
    menu = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    => """
    
    limite = 500
    LIMITE_SAQUES = 3
    
    while True:
        opcao = input(menu)
        
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            
            if valor > 0:
                clientes[cpf]["saldo"] += valor
                clientes[cpf]["extrato"] += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")
        
        elif opcao == "s":
            if autenticar_cliente(cpf):
                valor = float(input("Informe o valor do saque: "))
                
                excedeu_saldo = valor > clientes[cpf]["saldo"]
                excedeu_limite = valor > limite
                excedeu_saques = clientes[cpf]["numero_saques"] >= LIMITE_SAQUES
                
                if excedeu_saldo:
                    print("Operação falhou! Você não tem saldo suficiente.")
                elif excedeu_limite:
                    print("Operação falhou! O valor do saque excede o limite.")
                elif excedeu_saques:
                    print("Operação falhou! Número máximo de saques excedido.")
                elif valor > 0:
                    clientes[cpf]["saldo"] -= valor
                    clientes[cpf]["extrato"] += f"Saque: R$ {valor:.2f}\n"
                    clientes[cpf]["numero_saques"] += 1
                else:
                    print("Operação falhou! O valor informado é inválido.")
            else:
                break
        
        elif opcao == "e":
            if autenticar_cliente(cpf):
                print("\n================ EXTRATO ================")
                print("Não foram realizadas movimentações." if not clientes[cpf]["extrato"] else clientes[cpf]["extrato"])
                print(f"\nSaldo: R$ {clientes[cpf]['saldo']:.2f}")
                print("==========================================")
            else:
                break
        
        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Menu inicial de login ou criação de conta
def menu_inicial():
    while True:
        print("[1] Login")
        print("[2] Criar conta")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cpf_input = int(input("CPF (apenas números): "))
            nome_completo = input("Nome completo: ").lower()
            
            cliente = clientes.get(cpf_input)
            
            if not cliente or cliente["nome"].lower() != nome_completo:
                print("Conta não encontrada.")
            else:
                if autenticar_cliente(cpf_input):
                    print(f"Bem-vindo(a), {cliente['nome']}!")
                    sistema_bancario(cpf_input)
                else:
                    print("Autenticação falhou.")
        
        elif opcao == "2":
            cpf_input = criar_conta()
            sistema_bancario(cpf_input)
        
        else:
            print("Opção inválida, por favor selecione novamente.")

# Chamar o menu inicial
menu_inicial()
