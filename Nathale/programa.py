def carregar_dados(arquivo):
    dados = []
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
            
            # A primeira linha é o cabeçalho (colunas)
            colunas = linhas[0].strip().split(',')
            print(f"Colunas encontradas no arquivo: {colunas}")
            
            # As demais linhas são os dados
            for linha in linhas[1:]:
                valores = linha.strip().split(',')
                dados.append({
                    'nome': valores[0],
                    'caso': int(valores[1]),
                    'despesa': float(valores[2]),
                    'receita': float(valores[3])
                })
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo} não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
    
    return dados

# (a)
def buscar_cliente_por_nome(dados, parte_nome):
    clientes = set()
    for entrada in dados:
        if parte_nome.lower() in entrada['nome'].lower():
            clientes.add(entrada['nome'])
    return list(clientes)

# (b)
def buscar_casos_por_cliente(dados, nome_cliente):
    casos = []
    for entrada in dados:
        if entrada['nome'].lower() == nome_cliente.lower():
            casos.append(entrada['caso'])
    return casos

# (c)
def buscar_detalhes_caso(dados, numero_caso):
    for entrada in dados:
        if entrada['caso'] == numero_caso:
            nome_cliente = entrada['nome']
            despesa = entrada['despesa']
            receita = entrada['receita']
            diferenca = receita - despesa
            return nome_cliente, despesa, receita, diferenca
    return None

# (d)
def despesa_total(dados):
    return sum(entrada['despesa'] for entrada in dados)

# (e)
def receita_total(dados):
    return sum(entrada['receita'] for entrada in dados)

# (f)
def caso_maior_despesa(dados):
    maior_caso = max(dados, key=lambda x: x['despesa'])
    return maior_caso

# (g)
def caso_maior_receita(dados):
    maior_caso = max(dados, key=lambda x: x['receita'])
    return maior_caso

# (h)
def gerar_arquivo_cliente(dados, nome_cliente, arquivo_saida):
    casos_cliente = [entrada for entrada in dados if entrada['nome'].lower() == nome_cliente.lower()]
    
    if not casos_cliente:
        return f"Cliente {nome_cliente} não encontrado."
    
    total_despesas = sum(entrada['despesa'] for entrada in casos_cliente)
    total_receitas = sum(entrada['receita'] for entrada in casos_cliente)
    diferenca_total = total_receitas - total_despesas
    
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(f"Cliente: {nome_cliente}\n")
        f.write("Caso,Receita,Despesa\n")
        for entrada in casos_cliente:
            f.write(f"{entrada['caso']},{entrada['receita']},{entrada['despesa']}\n")
        f.write(f"\nTotal de Receitas: {total_receitas}\n")
        f.write(f"Total de Despesas: {total_despesas}\n")
        f.write(f"Diferença: {diferenca_total}\n")
    
    return f"Arquivo {arquivo_saida} gerado com sucesso."

# Menu
def exibir_menu():
    print("Menu de Opções:")
    print("1. Buscar clientes por parte do nome")
    print("2. Buscar casos associados a um cliente")
    print("3. Detalhes de um caso específico")
    print("4. Exibir despesa total")
    print("5. Exibir receita total")
    print("6. Caso com maior despesa")
    print("7. Caso com maior receita")
    print("8. Gerar arquivo para cliente específico")
    print("0. Sair")

def main():
    arquivo_txt = 'registro.txt'
    dados = carregar_dados(arquivo_txt)
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            parte_nome = input("Digite parte do nome do cliente: ")
            clientes = buscar_cliente_por_nome(dados, parte_nome)
            print("Clientes encontrados:", clientes)
        
        elif opcao == '2':
            nome_cliente = input("Digite o nome completo do cliente: ")
            casos = buscar_casos_por_cliente(dados, nome_cliente)
            print(f"Casos associados ao cliente {nome_cliente}: {casos}")
        
        elif opcao == '3':
            numero_caso = int(input("Digite o número do caso: "))
            detalhes = buscar_detalhes_caso(dados, numero_caso)
            if detalhes:
                print(f"Cliente: {detalhes[0]}, Despesa: {detalhes[1]}, Receita: {detalhes[2]}, Diferença: {detalhes[3]}")
            else:
                print("Caso não encontrado.")
        
        elif opcao == '4':
            total_despesa = despesa_total(dados)
            print(f"Despesa total: {total_despesa}")
        
        elif opcao == '5':
            total_receita = receita_total(dados)
            print(f"Receita total: {total_receita}")
        
        elif opcao == '6':
            maior_despesa = caso_maior_despesa(dados)
            print(f"Maior despesa: Cliente {maior_despesa['nome']}, Caso {maior_despesa['caso']}, Receita: {maior_despesa['receita']}, Despesa: {maior_despesa['despesa']}")
        
        elif opcao == '7':
            maior_receita = caso_maior_receita(dados)
            print(f"Maior receita: Cliente {maior_receita['nome']}, Caso {maior_receita['caso']}, Receita: {maior_receita['receita']}, Despesa: {maior_receita['despesa']}")
        
        elif opcao == '8':
            nome_cliente = input("Digite o nome completo do cliente: ")
            arquivo_saida = f"{nome_cliente.replace(' ', '_')}.txt"
            mensagem = gerar_arquivo_cliente(dados, nome_cliente, arquivo_saida)
            print(mensagem)
        
        elif opcao == '0':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()