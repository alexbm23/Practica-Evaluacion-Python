"""
binario.py
Programa que solicita al usuario un número binario, verifica su validez
y lo convierte a formato decimal.

"""
from typing import Any

def esBinario(strbinario: Any) -> bool:
    """
    Devuelve True o False si la cadena de caracteres (strbinario) 
    contiene una cadena binaria (solo '0' y '1').
    BARNESTEIN
    """
    if not isinstance(strbinario, str):
        return False
        
    return all(c in '01' for c in strbinario) and len(strbinario) > 0

def binario_a_decimal(strbinario: str) -> int:
    """
    Convierte una cadena binaria válida a su representación decimal.
    BARNESTEIN
    """
    return int(strbinario, 2)

def main_logic():
    # BARNESTEIN
    print("--- Conversor Binario a Decimal ---")
    
    while True:
        entrada = input("Introduce un número binario (o 'salir'): ")
        
        if entrada.lower() == 'salir':
            print("Saliendo del conversor binario.")
            break
            
        if esBinario(entrada):
            try:
                decimal = binario_a_decimal(entrada)
                print(f"El número binario {entrada} equivale a {decimal} en decimal.")
            except ValueError:
                print("Error: No se pudo realizar la conversión.")
        else:
            print(f"Error: '{entrada}' no es un número binario válido (solo se permiten '0' y '1').")

if __name__ == "__main__":
    main_logic()