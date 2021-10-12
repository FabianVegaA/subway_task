# Tarea Buda.com - Metro

![Tests](https://github.com/FabianVegaA/subway_task/actions/workflows/tests.yml/badge.svg)

- [Tarea Buda.com - Metro](#tarea-budacom---metro)
  - [Introducción](#introducción)
  - [Instrucciones](#instrucciones)
    - [Estructurar del archivo de entrada](#estructurar-del-archivo-de-entrada)
    - [Ejemplo de archivo de entrada](#ejemplo-de-archivo-de-entrada)

## Introducción

El proyecto conciste en un programa capaz de encontrar la ruta más corta entre dos puntos en un mapa de metro.

Exite 3 tipos de estaciones contemplados inicialmente para el programa, pero pueden añadirse más. Las estaciones se pueden asociar con un color (Rojo o Verde), estas indican que un tren exprés Verde pasará solo por estaciones sin color o Verdes, y un tren exprés de color Rojo pasará solo por estaciones sin color o Roja.

Por ejemplo:
![grafo con estaciones](screenshots/graph.png)

Si quisieramos encontrar la ruta más corta entre A y F, las rutas posibles serían:

- Si es un tren exprés Rojo: A -> B -> C -> H -> F
- Si es un tren exprés Verde: A -> B -> C -> D -> E -> F o A -> B -> C -> G -> I -> F
- Si es un tren sin color: A -> B -> C -> D -> E -> F

## Instrucciones

### Estructurar del archivo de entrada

```
#STATIONS
a
b red
c green
#END STATIONS

#ROUTES
a b
b c
c a
#END ROUTES
```

Para las estaciones se debe indicar el nombre de la estación y su color separado por un estacio. Del mismo modo las rutas se deben indicar con los nombres de las estaciones separadas por un espacio.

### Ejemplo de archivo de entrada

Para ejercer el programa con el archivo de entrada de ejemplo, se debe ejecutar el siguiente comando:

```shell
python3 main.py source destination filename
```

Para agregar el color del tren se debe agregar `--color <color>`, por defecto el tren es sin color.

Output:

```
La ruta más corta es:
A -> B -> C -> D -> E -> F
Número de pasos: 6
```
