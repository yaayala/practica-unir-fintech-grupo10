"""
License: Apache
Organization: UNIR

Aplicación de línea de comandos que lee una lista de palabras desde un
archivo de texto, opcionalmente elimina duplicados y las ordena en sentido
ascendente o descendente.
"""

import os
import sys

# Nombre de archivo utilizado cuando el usuario no proporciona uno.
DEFAULT_FILENAME = "words.txt"

# Valor por defecto para la eliminación de palabras duplicadas.
DEFAULT_DUPLICATES = False

# Orden por defecto aplicado a la lista de palabras.
DEFAULT_ORDER = "asc"

def sort_list(items, ascending=True):
    """
    Ordena una lista de elementos.
    Args: 
        items: Lista de elementos que se desea ordenar.
        ascending: Si es True, ordena de forma ascendente.
            Si es False, ordena de forma descendente.
    Returns:
        list: Una nueva lista con los elementos ordenados.
    Raises:
        RuntimeError: Si el valor recibido no es una lista.
    """
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort items of type {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    """
    Elimina elementos duplicados de una lista.
    Args:
        items: Lista original que puede contener duplicados.
    Returns:
        list: Lista sin duplicados.
    """
    return list(set(items))

def read_words_from_file(filename):
    """
    Lee las palabras contenidas en un archivo de texto.
    Cada linea del archivo se considera una palabra. Se eliminan los
    espacios o saltos de linea al inicio y final de cada linea.
    Args:
        filename: Nombre del archivo que contiene las palabras.
    Returns:
        list: Lista de palabras leidas desde el archivo.
    """
    file_path = os.path.join(".", filename)
    word_list = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word_list.append(line.strip())

    return word_list

def parse_arguments(arguments):
    """
    Procesa los argumentos recibidos desde la linea de comandos.

    Args:
        arguments: Argumentos recibidos en sys.argv.

    Returns:
        tuple: Nombre del archivo, indicador de eliminación de duplicados
        y orden solicitado.
    """
    if len(arguments) != 4:
        print("Invalid number of arguments.")
        print("Usage: python main.py <filename> <remove_duplicates> <order>")
        print("Example: python main.py words.txt yes asc")
        sys.exit(1)

    filename = arguments[1]
    remove_duplicates = arguments[2].lower() == "yes"
    order = arguments[3].lower()

    if order not in ("asc", "desc"):
        print("Invalid order value. Use 'asc' or 'desc'.")
        sys.exit(1)

    return filename, remove_duplicates, order

def main():
    """
    Punto de entrada principal de la aplicacion.

    Lee los argumentos, carga las palabras desde el archivo indicado,
    elimina duplicados si corresponde y muestra la lista ordenada.
    """
    filename, remove_duplicates, order = parse_arguments(sys.argv)

    print(f"Words will be read from file {filename}")
    print(f"Sort order: {order}")

    file_path = os.path.join(".", filename)

    if os.path.isfile(file_path):
        word_list = read_words_from_file(filename)
    else:
        print(f"File {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    # Convierte el valor textual del orden en un valor booleano.
    ascending = order == "asc"

    print(sort_list(word_list, ascending=ascending))

if __name__ == "__main__":
    main()