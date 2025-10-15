import math

def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números. Lanza error si el divisor es 0."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def potencia(a, b):
    """Calcula a elevado a la potencia b."""
    return a ** b

def raiz_cuadrada(a):
    """Calcula la raíz cuadrada de un número."""
    if a < 0:
        raise ValueError("No se puede calcular raíz de número negativo")
    return math.sqrt(a)

def modulo(a, b):
    """Calcula el resto (módulo) de a entre b."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a % b

def porcentaje(a, b):
    """Calcula el porcentaje que representa a respecto a b."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return (a / b) * 100

def promedio(lista):
    """Calcula el promedio de una lista de números."""
    if not lista:
        raise ValueError("La lista está vacía")
    return sum(lista) / len(lista)

def maximo(lista):
    """Devuelve el número máximo de una lista."""
    if not lista:
        raise ValueError("La lista está vacía")
    return max(lista)

def minimo(lista):
    """Devuelve el número mínimo de una lista."""
    if not lista:
        raise ValueError("La lista está vacía")
    return min(lista)

def factorial(n):
    """Calcula el factorial de un número."""
    if n < 0:
        raise ValueError("No existe el factorial de números negativos")
    return math.factorial(n)
