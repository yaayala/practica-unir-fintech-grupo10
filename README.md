# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

python3 main.py <filename> <dup>
  filename: **ruta** al fichero que contiene la lista de palabras, una por línea
  dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista

### Ejemplo de ejecución de prueba

Fichero de ejemplo `palabras_leixer.txt`, con palabras desordenadas (una por línea) y una repetida:

```
manzana
pera
banana
uva
pera
cereza
```

Conservando las palabras duplicadas (`no`):

```
python3 main.py palabras_leixer.txt no
Words will be read from file palabras_leixer.txt
['banana', 'cereza', 'manzana', 'pera', 'pera', 'uva']
```

Eliminando las palabras duplicadas (`yes`):

```
python3 main.py palabras_leixer.txt yes
Words will be read from file palabras_leixer.txt
['banana', 'cereza', 'manzana', 'pera', 'uva']
```