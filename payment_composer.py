from collections import Counter

valores_disponiveis = [150,90,50,80,100,90,750,700,60,100]

valores_disponiveis.sort(reverse=True)

valor_nota = int(input("digite o valor da nota: "))

valor_atual = 0

indice = 0

lista_qt = []
fim = True
while valor_atual < valor_nota:

    valor_atual += valores_disponiveis[indice]
    lista_qt.append(valores_disponiveis[indice])

    diferenca = valor_nota - valor_atual

    if diferenca < 100:
        valor_atual -= valores_disponiveis[indice]
        lista_qt.pop()

        diferenca = abs(valor_atual - valor_nota)
        valor_atual += 100*(diferenca/100) 
        texto = f"{diferenca/100} x {100}"
        lista_qt.append(texto)
        break

    if valor_atual > valor_nota:

        valor_atual -= valores_disponiveis[indice]
        lista_qt.pop()
        
        indice +=1

parte_contagem = lista_qt[:-1]
ultimo_item = lista_qt[-1]
contador = Counter(parte_contagem)

for item, quantidade in contador.items():
    print(f"{quantidade} x {item}")

print(ultimo_item)