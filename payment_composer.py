

valores_disponiveis = [150,90,50,80,100,90,750,700,60,100]

valores_disponiveis.sort(reverse=True)

valor_nota = 200

valor_atual = 0

indice = 0

lista_qt = []
fim = True
while valor_atual < valor_nota:

    valor_atual += valores_disponiveis[indice]
    lista_qt.append(valores_disponiveis[indice])

    diferenca = abs(valor_atual - valor_nota)

    if diferenca < 100:
        valor_atual -= valores_disponiveis[indice]
        lista_qt.pop()

        valor_atual += 100
        lista_qt.append(100)

        if valor_atual < valor_nota:
            while valor_atual < valor_nota:
                valor_atual += 60
                lista_qt.append(60)
            
            lista_qt.pop()
            valor_atual -= 60

        diferenca = abs(valor_atual - valor_nota)
        valor_atual += 100*(diferenca/100) 
        texto = f"{diferenca/100}% x {100}"
        lista_qt.append(texto)
        break

    if valor_atual > valor_nota:

        valor_atual -= valores_disponiveis[indice]
        lista_qt.pop()
        
        indice +=1

print(lista_qt)