🛡️ Proyecto de Evaluación UD1: Puesta en Producción SeguraCurso: Especialización en Ciberseguridad
Autor:Alejandro Barnestein Martos
Fecha:  30 Noviembre 2025
📝 Descripción General
Este proyecto implementa las Tareas 2 a 5 de la Práctica de Evaluación de la Unidad 1, con un énfasis en la modularidad del código y la aplicación de pruebas unitarias robustas para garantizar que el software resiste entradas defectuosas o inesperadas (comportamiento no deseado)
.Tareas CubiertasTarea 2: Conversión binario a decimal (binario.py).
Tarea 3: Verificación de valor en rango y lista (lista.py, basado en el Ejercicio 3 del libro).
Tarea 4: Suite de tests con unittest (Cobertura robusta).
Tarea 5: Suite de tests con pytest (Uso de framework de terceros y parametrización).
📂 Estructura del ProyectoEl código fuente (src) está separado de los tests (tests) para mantener la limpieza y la modularidad del proyecto.
 El archivo main.py actúa como el punto de entrada para el usuario.nombre_del_proyecto/
├── src/
│   ├── main.py            # Punto de entrada y menú modular.
│   ├── modulo1/           # Tarea 2: Lógica de binario.
│   │   └── binario.py     
│   └── modulo2/           # Tarea 3: Lógica de lista y rango.
│       └── lista.py       
└── tests/
    ├── test_unittest.py   # Tarea 4: Tests con unittest.
    └── test_pytest.py     # Tarea 5: Tests con pytest.
└── requirements.txt
🛠️ Requisitos e Instalación
DependenciasEl proyecto requiere Python 3 y las siguientes librerías:
# requirements.txt
pytest
Instalación
Se recomienda encarecidamente el uso de un entorno virtual (venv) para el desarrollo seguro.
# 1. Activación del Entorno Virtual (Práctica Segura)
python -m venv venv
.\venv\Scripts\activate

# 2. Instalación de dependencias
pip install -r requirements.txt
🚀 Ejecución de FuncionalidadesEl archivo main.py proporciona un menú interactivo para probar los módulos:
# Ejecutar desde la carpeta raíz del proyecto
python src/main.py

Opciones del Menú:Probar Conversor Binario: Inicia el bucle de validación y conversión (binario.py).Probar Verificador de Lista/Rango: Inicia la lógica del Ejercicio 3 (lista.py).
Salir: Termina la ejecución del programa.
🔬 Metodología de Testing (Tareas 4 y 5)
Las pruebas están diseñadas para cubrir la aparición de comportamientos no deseados, un pilar en la Puesta en Producción Segura.
Los tests verifican activamente que las funciones devuelven False o un resultado predecible en lugar de fallar (crash) con una excepción incontrolada.
Tarea 4: unittest (Enfoque en Robustez)
Función ProbadaEscenario de Falla EspecíficoCobertura de RobustezesBinarioTipo Incorrecto (None, int)
Verifica que el código devuelve False en lugar de lanzar un error interno.
estaEnRangoTipos IncompatiblesPrueba la comparación de int con list o str. Asegura que la función maneja el TypeError internamente y devuelve False.
estaEnListaArgumento No Lista (str, tuple, None)Confirma que el segundo argumento es estrictamente una lista, previniendo errores de método (AttributeError).
Comando de Ejecución:python -m unittest tests.test_unittest
Tarea 5: pytest (Parametrización y Eficiencia)Se utiliza pytest.mark.parametrize para ejecutar los mismos tests de robustez de forma más eficiente y limpia.Comando de Ejecución:python -m pytest tests/test_pytest.py

