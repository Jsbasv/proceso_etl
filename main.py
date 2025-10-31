import pdfplumber
import os


def extraer_texto_pdf(ruta_pdf: str) -> str | None:
    """
    Extrae el texto completo de un archivo PDF.

    Args:
        ruta_pdf (str): La ruta al archivo PDF.

    Returns:
        str: El texto completo extraído, o None si el archivo no se encuentra.
    """

    # 1. Verificar si el archivo PDF existe
    if not os.path.exists(ruta_pdf):
        print(f"Error: El archivo no se encontró en la ruta: {ruta_pdf}")
        return None

    texto_completo = []

    # 2. Abrir el PDF con pdfplumber
    # Usamos 'with' para asegurarnos de que el archivo se cierre correctamente
    try:
        with pdfplumber.open(ruta_pdf) as pdf:
            # 3. Iterar sobre cada página del PDF
            total_paginas = len(pdf.pages)
            print(f"El PDF tiene {total_paginas} páginas.")

            for i, pagina in enumerate(pdf.pages):
                # 4. Extraer el texto de la página actual
                # .extract_text() es bueno para la mayoría de PDFs estándar
                texto_pagina = pagina.extract_text()

                if texto_pagina:
                    texto_completo.append(texto_pagina)
                else:
                    print(
                        f"Advertencia: No se pudo extraer texto de la página {i + 1}."
                    )

        # 5. Unir el texto de todas las páginas en un solo string
        return "\n".join(texto_completo)

    except Exception as e:
        print(f"Error procesando el PDF: {e}")
        return None


# --- Punto de entrada principal ---
if __name__ == "__main__":
    # --- CONFIGURACIÓN ---
    # !! CAMBIA ESTO por la ruta a tu PDF
    MI_PDF = "temario_git.pdf"

    # Archivo donde guardaremos el texto en crudo (Práctica recomendada)
    ARCHIVO_SALIDA_TXT = "texto_extraido.txt"
    # ---------------------

    print(f"Iniciando extracción de: {MI_PDF}")

    # Llamamos a nuestra función de extracción
    texto_bruto = extraer_texto_pdf(MI_PDF)

    if texto_bruto:
        # --- PASO CLAVE (Prueba y Error) ---
        # Guardamos el texto en crudo en un .txt.
        # Esto te permite probar tu lógica de "resumen" y "keywords"
        # leyendo este .txt, que es mucho más rápido que leer el PDF.
        try:
            with open(ARCHIVO_SALIDA_TXT, "w", encoding="utf-8") as f:
                f.write(texto_bruto)

            print(f"\n¡Éxito! Texto guardado en: {ARCHIVO_SALIDA_TXT}")

            # Mostramos una vista previa de lo que se extrajo
            print("\n--- Vista Previa (primeros 500 caracteres) ---")
            print(texto_bruto[:500] + "...")
            print("-----------------------------------------------")

        except IOError as e:
            print(f"Error al guardar el archivo .txt: {e}")
    else:
        print("No se pudo extraer texto del PDF.")
