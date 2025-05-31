from todo.notas.menu import menu
from todo.notas.ingresar_notas import ingresar_notas
from todo.notas.calculos import calcular_estadisticas






def main():
    notas = []
    while True:
        menu()
        opcion = input("ingrese un opcion : ")
        if opcion == "1":
            notas  = ingresar_notas()
            print(f"notas ingresadas son {notas}")
        elif opcion == "2":
            if calcular_estadisticas(notas)  == None:
                print("no se agregaron notas por favor agragalas!!!")
                notas = ingresar_notas()
            estadisticas = calcular_estadisticas(notas)       
        elif opcion == "3":
            print(estadisticas)            
        else:
            print("terminado")
            break

    

if __name__ == "__main__":
    main()








