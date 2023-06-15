import math 
def suma(sum1, sum2):
    return sum1 + sum2
def resta(num1, num2):
    return num1 - num2
def multiplicacion(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 == 0:
        return "No se puede dividir enrtre cero"
    else:
        return num1 / num2

def exponencacion( num1, num2):
        return num1 ** num2
def raiz(num):
     return math.sqrt(num)
def suma5numeros(num1, num2, num3, num4, num5):
     return num1 + num2 + num3 + num4 + num5
def residuo(num1, num2):
     return num1 % num2

def quetzal_a_dolar(num):
    return num / 7.91

def dolar_a_quetzal(num):
    return num * 7.91


    
