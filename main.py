import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def mostrar_menu():
    print("Calculadora Open Source")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar N números")
    print("6. Salir")

def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {sumar.sumar(num1, num2)}")
        elif opcion == '2':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {resta.restar(num1, num2)}")
        elif opcion == '3':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {multiplicacion.multiplicar(num1, num2)}")
        elif opcion == '4':
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {dividir.dividir(num1, num2)}")
        elif opcion == '5':
            numeros = input("Ingresa los números separados por espacios: ")
            lista_numeros = [float(n) for n in numeros.split()]
            print(f"Resultado: {suma_avanzada.sumar_avanzado(lista_numeros)}")
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_calculadora()
