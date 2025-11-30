"""
main.py
Programa principal que actúa como punto de entrada (runner) para probar 
las funcionalidades de los módulos binario y lista (Tareas 2 y 3).
"""
import sys
import os
from typing import Callable, Dict

# Asegura que Python pueda encontrar el directorio 'src' y sus submódulos
# al ejecutar el archivo desde la carpeta raíz del proyecto.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

try:
    import modulo1.binario as binario_module
    import modulo2.lista as lista_module
except ImportError as e:
    print("----------------------------------------------------------------")
    print("ERROR DE CONFIGURACIÓN DE MÓDULOS:")
    print("Asegúrese de que los archivos __init__.py existen en src/, modulo1/ y modulo2/.")
    print(f"Error específico: {e}")
    sys.exit(1)


def mostrar_menu() -> None:
    """Muestra el menú de opciones al usuario."""
    print("\n=============================================")
    print("      MENÚ PRINCIPAL DE PRUEBAS MODULARES    ")
    print("=============================================")
    print("1. Probar Conversor Binario (Módulo binario.py)")
    print("2. Probar Verificador de Lista/Rango (Módulo lista.py)")
    print("3. Salir")
    print("=============================================")

def ejecutar_opcion(opcion: str) -> None:
    if opcion == '1':
        print("\n--- EJECUTANDO: Conversor Binario ---")
        binario_module.main_logic()
    elif opcion == '2':
        print("\n--- EJECUTANDO: Verificador de Lista/Rango ---")
        lista_module.main_logic()
    elif opcion == '3':
        print("Saliendo del programa principal. ¡Hasta pronto!")
        sys.exit(0) # Salida controlada
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        eleccion = input("Seleccione una opción (1-3): ")
        
        ejecutar_opcion(eleccion)