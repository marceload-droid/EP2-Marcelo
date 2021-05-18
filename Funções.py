def cria_baralho():
    valor = ['A', 'K', 'J', 'Q','2','3','4','5','6', '7','8','9', '10']
    cartas = []
    for i in valor:
        a = i+'♥'
        cartas.append(a)
        b = i+'♦'
        cartas.append(b)
        c = i+'♠'
        cartas.append(c)
        d = i+'♣'
        cartas.append(d)
    return cartas

def extrai_naipe(carta):
    naipes = ['♦', '♥', '♠', '♣']
    for i in naipes:
        if i in carta:
            return i
 
def extrai_valor(carta):
    valor = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    for i in valor:
        if i in carta:
            return i
        
def lista_movimentos_possiveis(baralho, index):
    from extrai_naipe import extrai_naipe as ex_np
    from extrai_valor import extrai_valor as ex_val
    c_sel = baralho[index] 
    valor = extrai_valor(carta)
    valoranterior = extrai_valor(baralho[i - 1])
    valormaisqueanterior = extrai_valor(baralho[i - 3])
    naipe = extrai_naipe(carta)
    naipeanterior = extrai_naipe(baralho[i - 1])
    naipemaisqueanterior = extrai_naipe(baralho[i - 3])

    if i == 0:
	return[0]
    elif i <= 2: 
        if valor == valoranterior:
            return [1]
        elif naipe == naipeanterior:
            return [1]
        else:
            return []

    elif i > 2:
        movimentos = []
        if valor == valoranterior:
            movimentos.append(1)
        elif naipe == naipeanterior:
            movimentos.append(1)
        
        if valor == valormaisqueanterior:
            movimentos.append(3)
        elif naipe == naipemaisqueanterior:
            movimentos.append(3)

        return movimentos

def empilha(baralho, inicio, final):
    baralho[final] = baralho[inicio]
    del(baralho[inicio])
    return baralho

    
def possui_movimentos_possiveis(baralho):
    uf = False
    i = 0
    for movimentos in baralho:
        if lista_movimentos_possiveis(baralho, i) != []:
            uf = True
        indice += 1
    return uf
