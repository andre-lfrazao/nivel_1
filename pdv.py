# Ponto de Venda (PDV) com Descontos Progressivos
# Desafio Nível 1 - Trilhas Inova / Backend Python

compras = []

print("=== SISTEMA DE PONTO DE VENDA (PDV) ===")
print("Digite 0 no valor da compra para encerrar e ver o resumo do dia.\n")

while True:
    valor_input = float(input("Digite o valor da compra em R$ (ou 0 para sair): "))
    
    # Condição de encerramento
    if valor_input == 0:
        break
        
    # Validação de valor negativo
    if valor_input < 0:
        print("Erro: O valor da compra não pode ser negativo. Tente novamente.\n")
        continue
        
    idade_input = int(input("Digite a idade do cliente em anos: "))
    
    # Validação de idade negativa
    if idade_input < 0:
        print("Erro: A idade não pode ser negativa. Tente novamente.\n")
        continue

    valor_original = valor_input
    valor_atual = valor_input

    # Regra 1: Desconto por idade (>= 65 anos -> 20%)
    if idade_input >= 65:
        valor_atual = valor_atual * 0.80

    # Regra 2: Desconto por valor (> R$ 100.00 após desconto de idade -> 10% extra)
    if valor_atual > 100.00:
        valor_atual = valor_atual * 0.90

    valor_final = round(valor_atual, 2)
    desconto_concedido = valor_original - valor_final

    # Guardar compra no histórico
    compras.append({
        "valor_original": valor_original,
        "idade": idade_input,
        "desconto": desconto_concedido,
        "valor_final": valor_final
    })

    print(f"Valor final da compra: R$ {valor_final:.2f}\n")

# Resumo Final do Dia
print("=" * 40)
print("RESUMO DO DIA")
print("=" * 40)

qtd_compras = len(compras)
total_bruto = sum(c["valor_original"] for c in compras)
total_descontos = sum(c["desconto"] for c in compras)
total_final = sum(c["valor_final"] for c in compras)

print(f"Quantidade de compras registradas: {qtd_compras}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
print("=" * 40)
