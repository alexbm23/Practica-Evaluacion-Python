"""
lista.py
Implementación de las funciones estaEnRango y estaEnLista, 
y la lógica principal para el Ejercicio 3.

"""
from typing import Any, List

# Definición de la lista y el rango BARNESTEIN
LISTA_DE_BUSQUEDA: List[int] = [6, 14, 11, 3, 2, 1, 15, 19]
MINIMO_RANGO: int = 1
MAXIMO_RANGO: int = 20

def estaEnRango(valor: Any, minimo: Any, maximo: Any) -> bool:
    """
    Devuelve True o False determinando que valor se encuentra entre el mínimo y el
    máximo
    BARNESTEIN
    """
    try:
        return minimo <= valor <= maximo
    except TypeError:
        return False
    except Exception:
        return False

def estaEnLista(valor: Any, lista: Any) -> bool:
    """
    Devuelve True o False determinando si el valor está en la lista.
    BARNESTEIN
    """
    if not isinstance(lista, list):
        return False
        
    return valor in lista

def main_logic():
    """
    Lógica principal de interacción con el usuario. BARNESTEIN
    """
    print("\n--- Verificador de Rango y Lista (Ejercicio 3) ---")
    print(f"Rango de validación: [{MINIMO_RANGO} - {MAXIMO_RANGO}]")
    print(f"Lista de búsqueda: {LISTA_DE_BUSQUEDA}")
    
    while True:
        entrada = input("\nIntroduce un número entero (o 'salir'): ")
        
        if entrada.lower() == 'salir':
            print("Saliendo del verificador de lista/rango.")
            break
        
        try:
            numero = int(entrada)
            
            if estaEnRango(numero, MINIMO_RANGO, MAXIMO_RANGO):
                print(f"✅ El número {numero} está DENTRO del rango ({MINIMO_RANGO}-{MAXIMO_RANGO}).")
                
                if estaEnLista(numero, LISTA_DE_BUSQUEDA):
                    print(f"✅ ¡El número {numero} está en la lista de búsqueda!")
                else:
                    print(f"❌ El número {numero} NO se encuentra en la lista de búsqueda.")
            else:
                print(f"❌ El número {numero} está FUERA del rango ({MINIMO_RANGO}-{MAXIMO_RANGO}).")
                
        except ValueError:
            print(f"Error: '{entrada}' no es un número entero válido.")

if __name__ == "__main__":
    main_logic()