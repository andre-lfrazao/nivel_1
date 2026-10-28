# Desafio Nível 1 - PDV com Descontos Progressivos (Python)

## O que o código faz

Este script simula um sistema básico de Ponto de Venda (PDV). O programa foi feito para registrar várias compras em sequência, aplicando descontos automáticos com base em duas regras principais:

1. **Desconto por idade:** Clientes com 65 anos ou mais ganham 20% de desconto.
2. **Desconto por valor:** Se o valor da compra (já considerando o desconto de idade, se houver) passar de R$ 100,00, ganha mais 10% de desconto extra.

No final, quando o usuário digita `0`, ele exibe um resumo com a quantidade de compras, o valor total bruto, o total de descontos e o faturamento líquido do dia.

## Como ele faz

1. **Entrada de dados e validação:** O programa solicita o valor da compra e a idade do cliente. Se o usuário digitar um valor negativo para qualquer um dos dois, o código exibe uma mensagem de erro e usa o `continue` para reiniciar a leitura sem salvar nada inválido.
2. **Encerramento:** Se o usuário  digitar `0` no valor da compra, o programa entende que o registro de compras foi finalizado e encerra o loop principal com o `break`.
3. **Cálculo dos descontos:**
   - Primeiro verifica a idade: se for maior ou igual a 65 anos, aplica 20% de desconto no valor inicial.
   - Depois verifica o valor atualizado: se o valor acumulado for maior que R$ 100,00, aplica mais 10% de desconto em cima do valor restante.
4. **Histórico e resumo final:** Cada compra finalizada é salva em uma lista. Quando o loop é encerrado com `0`, o script percorre esse histórico para calcular a quantidade total de vendas, a soma dos valores brutos, dos descontos e do total líquido final.

## Como usar

Certifique-se de ter o Python instalado. No terminal, abra a pasta onde está o arquivo e digite:

```
python pdv.py
```

Seguir as instruções na tela digitando o valor da compra e a idade do cliente. Para encerrar e ver o resumo, basta digitar `0` no valor da compra.

## Tabela de exemplos

Aqui estão alguns exemplos de simulação para testar se os cálculos estão corretos:

| \# | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |