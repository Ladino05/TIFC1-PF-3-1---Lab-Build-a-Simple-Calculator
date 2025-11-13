#def main():
    #a = int(input())
    #b = int(input())
    #resultado = a + b
    #print(resultado)

#if __name__ == "__main__":
    #main()

def main():
    a = int(input())
    b = int(input())
    resultado = a + b
    print(resultado)

    print("\nOpciones adicionales:")
    print("1. Restar")
    print("2. Multiplicar")
    print("3. Dividir")
    print("4. Módulo")
    print("5. Sumar tres números")
    print("6. Operaciones combinadas")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(a - b)

    elif opcion == "2":
        print(a * b)

    elif opcion == "3":
        if b != 0:
            print(a / b)
        else:
            print("No se puede dividir entre cero")

    elif opcion == "4":
        if b != 0:
            print(a % b)
        else:
            print("No se puede hacer módulo con cero")

    elif opcion == "5":
        c = int(input("Ingresa un tercer número: "))
        print(a + b + c)

    elif opcion == "6":
        c = int(input("Ingresa un tercer número: "))
        print((a * b) + c)

if __name__ == "__main__":
    main()
