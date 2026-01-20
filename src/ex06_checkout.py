"""
EX06 (Compendio: listas + tuplas + diccionarios)
Ticket de compra: calcula coste por producto y total general.
"""

PRICES: dict[str, float] = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}

def checkout(cart: list[tuple[str, int]]) -> tuple[dict[str, float], float]:
    """
    Recibe un carrito como lista de tuplas (producto, unidades).

    Devuelve:
    - Un diccionario con el coste por producto (producto -> coste)
    - Un float con el total general

    Reglas:
    - Si units < 0 -> ValueError
    - Si un producto no existe en PRICES -> ValueError
    - Si un producto aparece varias veces, se acumulan unidades

    Ejemplo:
    [("Pan", 2), ("Huevos", 1), ("Pan", 1)] ->
      ({"Pan": 4.2, "Huevos": 2.3}, 6.5)
    """

    if not cart:
        return ({}, 0.0)

    costos: dict[str, float] = {}
    total = 0.0
    cuenta: dict[str, int] = {}

    for item, cantidad in cart:
        if cantidad < 0:
            raise ValueError(f"Cantidad negativa para '{item}'")
        if item not in PRICES:
            raise ValueError(f"El producto '{item}' no está en la lista de precios")
        cuenta[item] = cuenta.get(item, 0) + cantidad

    for item, cantidad in cuenta.items():
        subtotal = round(PRICES[item] * cantidad, 2)
        costos[item] = subtotal
        total += subtotal

    total = round(total, 2)
    return (costos, total)
    raise NotImplementedError("Implementa checkout(cart)")
