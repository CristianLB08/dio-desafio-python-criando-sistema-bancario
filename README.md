# dio-desafio-python-criando-sistema-bancario

## Desafio da DIO - Criando um Sistema Bancário com Python

### Resumo do Funcionamento do Código do Sistema Bancário em Python

Este código implementa um sistema bancário simples com as seguintes funcionalidades: criação de conta, login, depósito, saque e visualização de extrato. Ele utiliza uma abordagem baseada em boas práticas de programação, incluindo validação de entrada, autenticação segura e modularidade.

#### Estrutura Geral

1. **Banco de Dados de Clientes**: Uma lista de dicionários é usada para armazenar informações dos clientes. Cada dicionário contém CPF, nome, telefone, senha, saldo, extrato e número de saques do cliente.

2. **Validação da Senha**: A função `validar_senha` garante que a senha atenda aos critérios de segurança: 
   - Deve ter entre 10 e 20 caracteres.
   - Deve conter pelo menos um número, uma letra maiúscula, uma letra minúscula e um caractere especial.

3. **Autenticação**: A função `autenticar_cliente` permite até 3 tentativas de inserção de senha. Se o usuário errar todas as tentativas, o sistema exibe uma mensagem de erro e sai automaticamente.

4. **Criação de Conta**: A função `criar_conta` coleta informações do usuário, valida a senha e adiciona um novo cliente à lista de clientes.

5. **Operações Bancárias**: A função `sistema_bancario` apresenta um menu com opções para depósito, saque, extrato e sair. Ela realiza operações bancárias específicas e autentica o cliente quando necessário.

6. **Menu Inicial**: A função `menu_inicial` permite que o usuário escolha entre login e criação de conta. Dependendo da escolha, ele direciona para as funções apropriadas.

#### Boas Práticas de Programação Implementadas

1. **Modularidade**: O código é dividido em funções distintas para cada funcionalidade (ex: `buscar_cliente`, `validar_senha`, `autenticar_cliente`, `criar_conta`, `sistema_bancario`, `menu_inicial`). Isso torna o código mais legível, reutilizável e fácil de manter.

2. **Validação de Entrada**: A função `validar_senha` assegura que a senha cumpra os requisitos de segurança. O CPF e outros dados de entrada são verificados e tratados adequadamente.

3. **Autenticação Segura**: O uso de até 3 tentativas para autenticação protege contra tentativas de login maliciosas.

4. **Mensagens de Erro Claras**: O código fornece feedback claro e útil ao usuário em caso de erros, como senhas inválidas ou operações falhadas.

5. **Manutenção de Estado**: Cada cliente tem seu próprio registro de saldo, extrato e número de saques, o que facilita a manutenção do estado da conta bancária.

6. **Uso de Estruturas de Dados Apropriadas**: Utilização de listas e dicionários para armazenar e gerenciar dados dos clientes, facilitando o acesso e a manipulação dos dados.

#### Resumo do Funcionamento

- **Login**: O usuário entra com CPF e nome completo. Se os dados coincidirem com um cliente existente, a senha é solicitada. Após três tentativas falhadas, o sistema sai automaticamente.
- **Criação de Conta**: O usuário fornece nome, sobrenome, CPF, telefone e cria uma senha válida. Os dados são armazenados na lista de clientes.
- **Depósito**: O cliente pode adicionar fundos à sua conta.
- **Saque**: O cliente pode retirar fundos da sua conta, sujeito a limites diários e de saldo. A autenticação é requerida.
- **Extrato**: O cliente pode visualizar as transações e o saldo atual. A autenticação é requerida.
- **Sair**: O usuário pode sair do sistema a qualquer momento.

Este código oferece uma base sólida para um sistema bancário simples, priorizando a segurança e a clareza na interação com o usuário.
