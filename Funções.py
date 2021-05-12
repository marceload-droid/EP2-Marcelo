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
        
        
