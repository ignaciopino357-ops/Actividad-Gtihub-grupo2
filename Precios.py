def calcualr_total(precio, cantidad):
    return precio * cantidad

def mostrar_total(precio, cantidad):
    total=calcualr_total(precio, cantidad)
    print(f"El total es: {total}")

mostrar_total(10000, 5)
