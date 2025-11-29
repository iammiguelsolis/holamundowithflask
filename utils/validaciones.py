def es_texto_valido(texto):
    if isinstance(texto, str) and len(texto.strip()) > 0:
        return True
    return False