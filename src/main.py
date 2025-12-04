from operaciones import sumar, restar, multiplicar, dividir

def main():
    print("=== Calculadora Básica ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción (1-4): ")

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print(f"Resultado: {sumar(a, b)}")
    elif opcion == "2":
        print(f"Resultado: {restar(a, b)}")
    elif opcion == "3":
        print(f"Resultado: {multiplicar(a, b)}")
    elif opcion == "4":
        try:
            print(f"Resultado: {dividir(a, b)}")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
