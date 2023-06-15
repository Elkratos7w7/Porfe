from seintento import *

def main():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Exponenciación")
    print("6. Raíz")
    print("7. Suma de 5 números")
    print("8. Residuo")
    print("9. Quetzal a Dólar")
    print("10. Dólar a Quetzal")

    opcion = int(input("Ingrese una opción:"))
    if opcion == 1:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: ")) 
            print(suma(num1, num2))
    elif opcion == 2:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: ")) 
            print(resta(num1, num2))
    elif opcion == 3:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: ")) 
            print(multiplicacion(num1, num2))
    elif opcion == 4:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: ")) 
            print(division(num1, num2))
    elif opcion == 5:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: ")) 
            print(exponenciacion(num1, num2))
    elif opcion == 6:
         num1 = float(input("Ingrese el primer número: "))
         print(raiz(num1))
    elif opcion == 7:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: ")) 
            num3 = float(input("Ingrese el tercer número: "))
            num4 = float(input("Ingrese el cuarto número: ")) 
            num5 = float(input("Ingrese el primer número: "))
            print(suma5numeros(num1, num2, num3, num4, num5))
    elif opcion == 8:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: ")) 
            print(residuo(num1, num2))
    elif opcion == 9:
            num1 = float(input("Ingrese la cantidad que desea convertir: "))
            print(quetzal_a_dolar(num1))       
    elif opcion == 10:
            num1 = float(input("Ingrese la cantidad que desea convertir: "))
            print(dolar_a_quetzal(num1))     
               
main()