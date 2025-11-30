"""
test_unittest.py
Suite de tests unitarios robustos para las funciones esBinario, estaEnRango y estaEnLista, 
utilizando el framework estándar unittest.
"""
import unittest
import sys
import os
from typing import List, Any

# Ajuste de ruta para que Python pueda encontrar el directorio 'src' y sus módulos
# Esto es esencial para la arquitectura de carpetas src/ y tests/  BARNESTEIN--------
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from modulo1.binario import esBinario
from modulo2.lista import estaEnRango, estaEnLista

class TestFunciones(unittest.TestCase):

    # --- TAREA 2: Tests para esBinario --- BARNESTEIN
    
    def test_es_binario_casos_positivos(self):
        """Comprueba cadenas binarias válidas."""
        self.assertEqual(esBinario("1001"), True, "Debe reconocer binario estándar")
        self.assertEqual(esBinario("0"), True, "Debe reconocer un solo bit '0'")
        self.assertEqual(esBinario("1010101010101010"), True, "Debe reconocer binario largo")

    def test_es_binario_casos_negativos_y_mixtos(self):
        self.assertEqual(esBinario("Hola"), False, "Debe fallar con letras")
        self.assertEqual(esBinario("10021"), False, "Debe fallar con números no binarios")
        self.assertEqual(esBinario("1 0 1"), False, "Debe fallar con espacios")
        self.assertEqual(esBinario(""), False, "Debe fallar con cadena vacía")
        self.assertEqual(esBinario("101."), False, "Debe fallar con puntuación")

    def test_es_binario_robustez_tipo(self):
        self.assertEqual(esBinario(101), False, "Debe fallar con entero")
        self.assertEqual(esBinario(None), False, "Debe fallar con None")

    # --- TAREA 3: Tests para estaEnRango ---BARNESTEIN

    def test_esta_en_rango_casos_numericos(self):
        self.assertEqual(estaEnRango(5, 1, 10), True, "Debe estar dentro")
        self.assertEqual(estaEnRango(1, 1, 10), True, "Debe incluir el mínimo")
        self.assertEqual(estaEnRango(10, 1, 10), True, "Debe incluir el máximo")
        self.assertEqual(estaEnRango(0, 1, 10), False, "Debe estar fuera del mínimo")
        self.assertEqual(estaEnRango(10.1, 1, 10), False, "Debe estar fuera del máximo (float)")

    def test_esta_en_rango_casos_cadenas(self):
        self.assertEqual(estaEnRango('m', 'a', 'z'), True, "Debe estar dentro del rango alfabético")
        self.assertEqual(estaEnRango('A', 'a', 'z'), False, "Debe ser sensible a mayúsculas")

    def test_esta_en_rango_robustez_tipo(self):
        self.assertEqual(estaEnRango(5, [1], 10), False, "Debe fallar si tipos son incompatibles (list vs int)")
        self.assertEqual(estaEnRango(5, 1, "diez"), False, "Debe fallar si tipos son incompatibles (int vs str)")
        self.assertEqual(estaEnRango(5, None, 10), False, "Debe fallar con None")
    
    # --- TAREA 3: Tests para estaEnLista ---BARNESTEIN

    def test_esta_en_lista_casos_funcionales(self):
        test_lista = [1, "b", True, {"key": "value"}]
        self.assertEqual(estaEnLista(1, test_lista), True, "Debe encontrar entero")
        self.assertEqual(estaEnLista("b", test_lista), True, "Debe encontrar string")
        self.assertEqual(estaEnLista("B", test_lista), False, "Debe ser sensible a mayúsculas")
        self.assertEqual(estaEnLista(99, test_lista), False, "No debe encontrar valor ausente")

    def test_esta_en_lista_robustez_entrada(self):
        self.assertEqual(estaEnLista(1, "not a list"), False, "Debe fallar si el segundo argumento no es una lista (es str)")
        self.assertEqual(estaEnLista(1, (1, 2, 3)), False, "Debe fallar si es una tupla")
        self.assertEqual(estaEnLista(1, None), False, "Debe fallar si es None")


if __name__ == '__main__':
    unittest.main()