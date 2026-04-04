

def leer_inventario(ruta_archivo):
    productos_raw=[]

    with open (ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas= archivo.readlines()

        if not lineas:
            return productos_raw
        
        encabezados = lineas[0].strip().split(",")

        for linea in lineas[1:]:
            linea = linea.strip()
            if not linea:
                continue

            valores= linea.split(",")
            if len(valores) == len(encabezados)
            producto_dict = dict(zip(encabezados,valores))
            productos_raw.append(producto_dict)

    return productos_raw
        
def escribir_reporte(productos,ruta_archivo):
    encabezados = ["sku","nombre","categoria","stock_actual","stock_minimo", 
                   "unidades_faltantes", "valor_inventario"]

    with open(ruta_archivo, 'w',encoding='utf-8') as archivo:
        archivo.write(','.join(encabezados)+'\n')

        for producto in productos:
            linea= f"{producto.sku},{producto.nombre},{producto.categoria},{producto.stock}"
            linea += f"{producto.stock_minimo}, {producto.unidades_faltantes()},{round(producto.valor_inventario,2)}"
            archivo.write(linea+'\n')
        