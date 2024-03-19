import math

def criba_eratostenes(n):
    raiz_cuadrada_de_n_redondeada_para_abajo=int(math.floor(math.sqrt(n)))
    lista_numeros_primos=[]
    lista_numeros_no_primos=[]
    for i in range (2,n+1):
        lista_numeros_primos.append(i)
    for j in range (1,raiz_cuadrada_de_n_redondeada_para_abajo+1):
        if j in lista_numeros_primos:
            for k in range (j,int(math.floor(n/j)+1)):
                if k in lista_numeros_primos:
                    if k*j not in lista_numeros_no_primos:
                        lista_numeros_no_primos.append(k*j)
    for l in range (len(lista_numeros_no_primos)):
        lista_numeros_primos.remove(lista_numeros_no_primos[l])
    return lista_numeros_primos

print(criba_eratostenes(1))
