import re


def tokenize_page(text: str) -> list[str]:
    """
    Tokeniza un texto en palabras.

    Args:
        text (str): El texto a tokenizar.

    Returns:
        list[str]: Una lista de palabras (tokens).
    """
    if not isinstance(text, str):
        print("Advertencia: Se esperaba un string para tokenizar.")
        return []

    # Usamos una expresión regular para encontrar todas las secuencias de palabras
    # y las convierte a minúsculas para normalizar los tokens.
    words = re.findall(r"\b\w+\b", text.lower())
    return words
