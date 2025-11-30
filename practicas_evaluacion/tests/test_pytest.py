"""
test_pytest.py
Suite de tests unitarios robustos para las funciones esBinario, estaEnRango y estaEnLista, 
utilizando el framework de terceros pytest (Tarea 5).

Para ejecutar:
1. Instalar pytest: pip install pytest
2. Ejecutar desde la raíz del proyecto (Testing_python): pytest
"""
import pytest
import sys
import os
from typing import List, Any

# Ajuste de ruta para que Python pueda encontrar el directorio 'src' y sus módulos
# Esto es esencial para la arquitectura de carpetas src/ y tests/ 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

#BARNESTEIN
from modulo1.binario import esBinario, binario_a_decimal
from modulo2.lista import estaEnRango, estaEnLista

# --- TAREA 2: Tests para esBinario ---BARNESTEIN
@pytest.mark.parametrize("input_str, expected", [
    ("1001", True),
    ("0", True),
    ("10101010", True),
    ("Hola", False),
    ("10021", False),  # Número no binario
    ("1 0 1", False),  # Espacios
    ("", False),       # Cadena vacía
    (101, False),      # Tipo incorrecto: int
    (None, False),     # Tipo incorrecto: None
])
def test_es_binario(input_str: Any, expected: bool):
    assert esBinario(input_str) == expected

def test_binario_a_decimal_conversion():
    assert binario_a_decimal("101") == 5
    assert binario_a_decimal("1111") == 15
    assert binario_a_decimal("0") == 0

# --- TAREA 3: Tests para estaEnRango ---BARNESTEIN
@pytest.mark.parametrize("valor, minimo, maximo, expected", [
    # Casos funcionales
    (5, 1, 10, True),
    (1, 1, 10, True),  # Límite inferior
    (10, 1, 10, True), # Límite superior
    (0, 1, 10, False), # Fuera de rango
    ('m', 'a', 'z', True), # Cadenas

    (5, [1], 10, False),    # list vs int
    (5, 1, "diez", False),  # int vs str
    (5, None, 10, False),   # None
])
def test_esta_en_rango(valor: Any, minimo: Any, maximo: Any, expected: bool):
    assert estaEnRango(valor, minimo, maximo) == expected

# --- TAREA 3: Tests para estaEnLista ---BARNESTEIN
@pytest.mark.parametrize("valor, lista, expected", [
    (1, [1, 2, 3], True),
    ("b", [1, "b", True], True),
    (4, [1, 2, 3], False),
    ("B", [1, "b"], False), 
    
    (1, "not a list", False), # str
    (1, (1, 2, 3), False),    # tuple
    (1, None, False),         # None
])
def test_esta_en_lista(valor: Any, lista: List[Any], expected: bool):
    assert estaEnLista(valor, lista) == expected