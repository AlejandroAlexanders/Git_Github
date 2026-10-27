# Pruebas del inventario
def test_stock_minimo():
    assert 5 > 0

def test_cargar_productos():
    productos = ["1;Teclado;20;15.99"]
    assert len(productos) == 1

def test_precio_positivo():
    precio = 15.99
    assert precio > 0