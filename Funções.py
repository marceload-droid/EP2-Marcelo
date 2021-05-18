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
    from extrai_naipe import extrai_naipe
    from extrai_valor import extrai_valor
    carta_selecionada = baralho[index]  
    valordacarta = extrai_valor(carta_selecionada)
    valor_anterior = extrai_valor(baralho[index - 1])
    valor_mais_que_anterior = extrai_valor(baralho[index - 3])
    naipe_carta = extrai_naipe(carta_selecionada)
    naipe_anterior = extrai_naipe(baralho[index - 1])
    naipe_mais_que_anterior = extrai_naipe(baralho[index - 3])

    if index == 0:
        return []

    elif index <= 2:
        if valordacarta == valor_anterior:
            return [1]
        elif naipe_carta == naipe_anterior:
            return [1]
        else:
            return []


    elif index > 2:
        possiveis_mov = []
        if valordacarta == valor_mais_que_anterior:
            possiveis_mov.append(3)
        elif naipe_carta == naipe_mais_que_anterior:
            possiveis_mov.append(3)
        
        if valordacarta == valor_anterior:
            possiveis_mov(1)
        elif naipe_carta == naipe_anterior:
            possiveis_mov(1)

            return possiveis_mov
        
def empilha(baralho, inicio, final):
    baralho[final] = baralho[inicio]
    del(baralho[inicio])
    return baralho
