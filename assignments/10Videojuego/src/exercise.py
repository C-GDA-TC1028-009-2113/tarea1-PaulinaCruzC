def main():
    #escribe tu código abajo de esta línea
    nuevos= int(input("Dame la cantidad de juegos nuevos: "))
    usados= int(input("Dame la cantidad de juegos usados: "))
    coston= 1000*nuevos
    costou= 350*usados
    print("El total de la compra es: "+ str(coston+costou))




if __name__ == '__main__':
    main()
