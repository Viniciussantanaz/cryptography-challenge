import math

def RowsColums(N,Length):
    X = N 
    M = 0
    while M < Length:
        M = X*N
        X += 1
    return X - 1

S = input("Digite seu texto: ")

Backspace = list(filter(lambda X: X != ' ',S))



L = len(Backspace)

Raiz_L = int (math.sqrt(L))

RowColum = [Raiz_L,(RowsColums(Raiz_L,L))]

x = 0
for c in range(RowColum[1]+1):
    x += RowColum[0]
    print(''.join(Backspace[x-RowColum[0]:x]))