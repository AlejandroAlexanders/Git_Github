# Inventario del almacén
STOCK_MINIMO = 5

def cargar_productos(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.readlines()

def productos_bajo_minimo(productos):
    return [p for p in productos if int(p.split(";")[2]) < STOCK_MINIMO]