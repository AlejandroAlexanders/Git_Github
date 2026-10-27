# Inventario del almacén
STOCK_MINIMO = 5

def cargar_productos(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.readlines()