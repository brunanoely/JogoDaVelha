from random import randrange


def jogo_da_velha(tabuleiro):
    print("+-------" * 3, "+", sep="")
    for linha in range(3):
        print("|       " * 3, "|", sep="")
        for coluna in range(3):
            print("|   " + str(tabuleiro[linha][coluna]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def fazer_jogada(tabuleiro):
    ok = False
    while not ok:
        jogada = input("Digite sua jogada: ")
        ok = len(jogada) == 1 and jogada >= '1' and jogada <= '9'
        if not ok:
            print("Jogada inválida – repita sua entrada!")
            continue
        jogada = int(jogada) - 1
        linha = jogada // 3
        coluna = jogada % 3
        sinal = tabuleiro[linha][coluna]
        ok = sinal not in ['O', 'X']
        if not ok:
            print("Campo já ocupado – repita sua entrada!")
            continue
    tabuleiro[linha][coluna] = 'O'


def listar_campos_livres(tabuleiro):
    livres = []
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] not in ['O', 'X']:
                livres.append((linha, coluna))
    return livres


def vitoria_por(tabuleiro, sgn):
    if sgn == "X":
        quem = 'eu'
    elif sgn == "O":
        quem = 'você'
    else:
        quem = None
    cruzada1 = cruzada2 = True
    for rc in range(3):
        if tabuleiro[rc][0] == sgn and tabuleiro[rc][1] == sgn and tabuleiro[rc][2] == sgn:
            return quem
        if tabuleiro[0][rc] == sgn and tabuleiro[1][rc] == sgn and tabuleiro[2][rc] == sgn:
            return quem
        if tabuleiro[rc][rc] != sgn:
            cruzada1 = False
        if tabuleiro[2 - rc][2 - rc] != sgn:
            cruzada2 = False
    if cruzada1 or cruzada2:
        return quem
    return None


def jogar_computador(tabuleiro):
    livres = listar_campos_livres(tabuleiro)
    cnt = len(livres)
    if cnt > 0:
        this = randrange(cnt)
        linha, coluna = livres[this]
        tabuleiro[linha][coluna] = 'X'


tabuleiro = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
tabuleiro[1][1] = 'X'
livres = listar_campos_livres(tabuleiro)
turno_humano = True
while len(livres):
    jogo_da_velha(tabuleiro)
    if turno_humano:
        fazer_jogada(tabuleiro)
        vitorioso = vitoria_por(tabuleiro, 'O')
    else:
        jogar_computador(tabuleiro)
        vitorioso = vitoria_por(tabuleiro, 'X')
    if vitorioso is not None:
        break
    turno_humano = not turno_humano
    livres = listar_campos_livres(tabuleiro)

jogo_da_velha(tabuleiro)
if vitorioso == 'você':
    print("Você ganhou!")
elif vitorioso == 'eu':
    print("Eu ganhei!")
else:
    print("Empate!")

 

 

 


 

 


 

 




 

 

 

 

 

 

 


 

 

 


 

 

 

 


 

 

 


 

