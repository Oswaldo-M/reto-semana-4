# Sistema de Inventario Modular

## Descripción

Este proyecto implementa un sistema de inventario modular en Python que permite leer productos desde un archivo CSV, validar sus datos y generar un reporte con aquellos productos que necesitan reorden (stock menor al mínimo).

El sistema está diseñado siguiendo buenas prácticas de programación, separando responsabilidades en módulos para facilitar su mantenimiento y escalabilidad.

---

## Estructura del Proyecto

```
reto-semana-04/
├── main.py
├── README.md
├── .gitignore
├── models/
│   ├── __init__.py
│   └── producto.py
├── utils/
│   ├── __init__.py
│   ├── io.py
│   └── validators.py
├── data/
│   └── inventario.csv
└── outputs/
    └── reporte_inventario.csv
```

### Descripción de archivos y carpetas

* **main.py**
  Punto de entrada del programa. Coordina la lectura del archivo, validación de datos y generación del reporte.

* **README.md**
  Documentación del proyecto.

* **.gitignore**
  Define qué archivos o carpetas no deben subirse al repositorio.

---

### Carpeta `models/`

Contiene las clases que representan las entidades del sistema.

* **producto.py**
  Define la clase `Producto`, incluyendo atributos, métodos y lógica como validación de stock y representaciones (`__str__`, `__repr__`).

---

### Carpeta `utils/`

Funciones auxiliares reutilizables.

* **io.py**
  Maneja la lectura y escritura de archivos CSV.

* **validators.py**
  Contiene funciones para validar los datos de entrada:

  * Validación de SKU (no vacío ni con solo espacios)
  * Validación de precio (número mayor o igual a 0)
  * Validación de stock (entero mayor o igual a 0)
    Además, incluye la función `validar_producto`, que centraliza todas estas validaciones y devuelve si un producto es válido junto con un mensaje de error en caso contrario.

---

### Carpeta `data/`

Contiene los archivos de entrada.

* **inventario.csv**
  Archivo con los datos de los productos a procesar.

---

### Carpeta `outputs/`

Contiene los resultados generados por el programa.

* **reporte_inventario.csv**
  Archivo generado con los productos que necesitan reorden.

---

## Cómo Ejecutar

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

---

## Entrada (`data/inventario.csv`)

```csv
sku,nombre,categoria,precio,stock,stock_minimo
SKU001,Laptop HP,Electronica,15000.00,5,10
SKU002,Mouse Logitech,Accesorios,350.00,3,15
SKU003,Teclado Mecanico,Accesorios,800.00,20,10
SKU004,Monitor LG,Electronica,6000.00,8,5
SKU005,Audifonos Sony,Accesorios,1200.00,2,10
SKU006,Webcam HD,Accesorios,450.00,25,20
SKU007,SSD 1TB,Almacenamiento,1800.00,0,5
```

---

## Salida (`outputs/reporte_inventario.csv`)

```csv
sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario
SKU002,Mouse Logitech,Accesorios,3,15,12,1050.00
SKU005,Audifonos Sony,Accesorios,2,10,8,2400.00
SKU001,Laptop HP,Electronica,5,10,5,75000.00
SKU007,SSD 1TB,Almacenamiento,0,5,5,0.00
```

---

## Autor

Oswaldo Jafet Morales FLores 
