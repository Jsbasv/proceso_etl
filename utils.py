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


def structure_text_to_dict(raw_text: str, tokens: list[str]) -> dict:
    """
    Estructura el texto extraído y sus tokens en un diccionario.
    Este es un punto de partida, y la estructura puede ser expandida
    para incluir más campos relevantes del PDF.

    Args:
        raw_text (str): El texto completo extraído del PDF.
        tokens (list[str]): La lista de tokens del texto.

    Returns:
        dict: Un diccionario con el texto bruto y los tokens,
              y potencialmente otros campos estructurados.
    """
    if not isinstance(raw_text, str):
        print(
            "Advertencia: Se esperaba un string para raw_text en structure_text_to_dict."
        )
        raw_text = ""
    if not isinstance(tokens, list):
        print(
            "Advertencia: Se esperaba una lista para tokens en structure_text_to_dict."
        )
        tokens = []

    structured_data = {
        "raw_text": raw_text,
        "tokenized_text": tokens,
        # Aquí puedes añadir más campos estructurados en el futuro,
        # como "titulo", "autores", "secciones", etc.
        # Por ejemplo:
        # "word_count": len(tokens),
        # "unique_words_count": len(set(tokens))
    }
    return structured_data
