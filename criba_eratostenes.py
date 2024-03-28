import math
num_giones=100
print()
print("¡Hola!")
print()
print("Te doy la bienvenida a este pequeño programita para hallar todos los números primos")
print("que se encuentren antes del número que tú me digas (mejor conocido como criba de eratóstenes).")
print()
print("Si deseas apoyarme te dejo mi alias de Mercado Pago Argentina: sojo.sam.mp")
print()
print("También te dejo mi ig por si deseas seguirme: @therealdusa")
print()
print("Y por último (pero no por eso menos importante) te dejo mi perfil de GitHub")
print("para que lo chusmees (me gusta programar cosas relacionadas a las materias de la facultad o ")
print("que sean de mi interés):")
print()
print("https://github.com/SojoSamCC")
print()
print("Bueeeeno, ahora sí. Comencemosss")
print()

for _ in range(num_giones):
    print("-", end="")
print()
def criba_eratostenes():
    print()
    print("Ingresa el número del cual quieres saber los números primos", end=" ")
    n=int(input("que le preceden: "))
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
    print()
    return print(f"Todos los números primos que encuentran antes del dado son: {lista_numeros_primos}")
criba_eratostenes()

while True:
    print()
    repetir_criba=input("¿Deseas repetir la criba de eratóstenes? (Y/n): ")
    if repetir_criba!="n":
        criba_eratostenes()
    else:
        print()
        break

for _ in range(num_giones):
    print("-", end="")

print()
print()
print("¡Muchas gracias por haccer uso de este programita! Espero te haya sido de ayuda.")
print()
print("Te deseo un muy buen día.")
print()
print("-SojoSam")
print()
input("--Presiona cualquier tecla para cerrar el programa--")
exit()
