class Producto:

    def __init__(self, sku,nombre,categoria,precio,stock,stock_minimo):
        self.sku=sku
        self.nombre= nombre
        self.categoria= categoria
        self.precio=precio
        self.stock= stock
        self.stock_minimo= stock_minimo

    def necesita_reorden(self):
        return self.stock < self.stock_minimo

    def unidades_faltantes(self):
        return self.stock_minimo - self.stock
    
    def valor_inventario(self):
        return self.stock*self.precio
    
    def __str__(self):
        estado = "Se necesita reorden!" if self.necesita_reorden() else "OK" 
        return f"{self.sku}: {self.nombre} Stock: {self.stock}/{self.stock_minimo} {estado}"

    
    def __repr__(self):
        return f"Producto('{self.sku}', '{self.nombre}', '{self.categoria}', {self.precio}, {self.stock}, {self.stock_minimo})"