"""
EX05 (Diccionarios)
Tabla de búsqueda: divisa -> símbolo.
"""

CURRENCIES: dict[str, str] = {"Euro": "€", "Dollar": "$", "Yen": "¥"}

def currency_symbol(currency: str) -> str | None:
    """
    Devuelve el símbolo de la divisa si existe, o None si no existe.

    - No lanza error si la divisa no está.
    """

    if currency in CURRENCIES:
        return CURRENCIES[currency]
    else:
        return None 

    raise NotImplementedError("Implementa currency_symbol(currency)")
