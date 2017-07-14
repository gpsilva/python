def gera_nome_convite ():
    convite = 'Flavio Henrique Almeida'
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:4]
    parte2 = convite[posicao_inicial:posicao_final]
    print "%s %s" % (parte1, parte2)
